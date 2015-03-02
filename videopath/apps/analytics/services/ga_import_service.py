import gdata.analytics.client
import json
import datetime
import time

from django.conf import settings

from videopath.apps.videos.models import Video, Marker
from videopath.apps.analytics.models import TotalAnalyticsData, DailyAnalyticsData
from videopath.apps.analytics.signals import analytics_imported

#
# Import data from google analytics
#
def import_data():

    client = _get_client()

    # import daily numbers
    datemapper = DateMapperDaily()
    for importer in importers:
        i = importer(datemapper, client)
        i.import_data()

    # import total numbers
    datemapper = DateMapperTotal()
    for importer in importers:
        i = importer(datemapper, client)
        i.import_data()

    # move total played numbers into video data
    for tad in TotalAnalyticsData.objects.all():
        tad.video.total_plays = tad.plays_all
        tad.video.save()

    analytics_imported.send_robust(None)

    

#
# Import historical data from google analytics
#
def import_historical_data(offset=0):

    client = _get_client()

    c = offset
    while c < 5000:
      c = c + 1
      time.sleep(10)
      print str(c) + " ago"
      datemapper = DateMapperDaily()
      datemapper.set_days_ago(c)
      for importer in importers:
          i = importer(datemapper,client)
          i.import_data()


# get google analytics client helper function
def _get_client():
    SOURCE_APP_NAME = 'videopath-api'
    client = gdata.analytics.client.AnalyticsClient(source=SOURCE_APP_NAME)
    client.client_login(
        settings.GA_USERNAME,
        settings.GA_PASSWORD,
        source=SOURCE_APP_NAME,
        service=client.auth_service,
        account_type='GOOGLE',
    )
    return client


# map date to database rows

class DateMapper:

    def __init__(self):
        self.row_cache = {}

    def get_range(self):
        return None, None

    def get_database_row(self, id):
        if id in self.row_cache:
            return self.row_cache[id]
        row = self.get_database_row_uncached(id)
        self.row_cache[id] = row
        return row

    def get_database_row_uncached(self, id):
        return None


class DateMapperTotal(DateMapper):

    def get_range(self):
        return "2006-01-01", "2020-01-01"

    def get_database_row_uncached(self, id):
        try:
            #if id != "1PgRRon5":
            #    return None
            v = Video.objects.get(key=id)
            row, created = TotalAnalyticsData.objects.get_or_create(video=v)
            return row
        except Video.DoesNotExist:
            return None


class DateMapperDaily(DateMapper):

    def __init__(self):
        self.set_days_ago(1)

    def set_days_ago(self, days_ago):
        self.row_cache = {}
        self.date = datetime.date.today() - datetime.timedelta(days=days_ago)

    def get_range(self):
        return self.date, self.date

    def get_database_row_uncached(self, id):
        try:
            v = Video.objects.get(key=id)
            row, created = DailyAnalyticsData.objects.get_or_create(
                video=v, date=self.date)
            return row
        except Video.DoesNotExist:
            return None


# get google analytics feed

class MetricsImport:

    def __init__(self, datemapper, client):
        self.client = client
        self.max_results = 10000
        self.current_offset = 1
        self.datemapper = datemapper

    def get_query_args(self):
        return {}

    def get_entries(self):
        start_date, end_date = self.datemapper.get_range()
        query_args = self.get_query_args()
        default_args = {
            'ids': 'ga:83927052',
            'dimensions': 'ga:dimension1',
            'metrics': 'ga:visits',
            'sort': 'ga:dimension1',
            'start-date': start_date,
            'end-date': end_date,
            'max-results': self.max_results,
            'prettyprint': 'true',
            'start-index': self.current_offset
        }
        query_args = dict(default_args.items() + query_args.items())
        data_query = gdata.analytics.client.DataFeedQuery(query_args)
        self.current_offset += self.max_results
        feed = self.client.GetDataFeed(data_query)
        return feed.entry, int(feed.total_results.text) > self.current_offset

    def process_start(self):
        pass

    def process_row(self, entry, row):
        pass

    def process_end(self):
        pass

    def import_data(self):
        has_more = True

        self.process_start()
        while has_more:
            entries, has_more = self.get_entries()
            for entry in entries:
                row = self.datemapper.get_database_row(
                    entry.dimension[0].value)
                if row:
                    self.process_row(entry, row)
                    row.save()
        self.process_end()


# import plays
class MetricsImportPlays(MetricsImport):

    def get_query_args(self):
        return {
            'metrics': 'ga:uniqueEvents, ga:newUsers',
            'filters': 'ga:eventAction==play'
        }

    def process_row(self, entry, row):
        # print feed.totalResults
        plays_by_all_users = entry.metric[0].value
        plays_by_new_users = entry.metric[1].value
        row.plays_all = plays_by_all_users
        row.plays_unique = plays_by_new_users


# import markers clicked
class MetricsImportMarkersClicked(MetricsImport):

    def get_query_args(self):
        return {
            'metrics': 'ga:totalEvents, ga:uniqueEvents',
            'filters': 'ga:eventAction==show overlay'
        }

    def process_row(self, entry, row):
        row.overlays_opened_all = entry.metric[0].value
        row.overlays_opened_unique = entry.metric[1].value


# import session duration
class MetricsImportSessionDuration(MetricsImport):

    def get_query_args(self):
        return {
            'metrics': 'ga:avgSessionDuration',
        }

    def process_row(self, entry, row):
        row.avg_session_time = entry.metric[0].value

# import video completed


class MetricsImportVideoCompleted(MetricsImport):

    def get_query_args(self):
        return {
            'metrics': 'ga:uniqueEvents',
            'filters': 'ga:eventAction==video ended'
        }

    def process_row(self, entry, row):
        row.video_completed = entry.metric[0].value

# import video sessions


class MetricsImportSessions(MetricsImport):

    def get_query_args(self):
        return {
            'metrics': 'ga:uniqueEvents',
            'filters': 'ga:eventAction==pathplayer ready'
        }

    def process_row(self, entry, row):
        row.sessions = entry.metric[0].value

# import list of popular markers
class MetricsPopularMarkers(MetricsImport):

    def get_query_args(self):
        return {
            'dimensions': 'ga:dimension1, ga:eventLabel',
            'metrics': 'ga:totalEvents, ga:uniqueEvents',
            'filters': 'ga:eventAction==show overlay'
        }

    def process_start(self):
        self.video_cache = {}

    def process_end(self):
        self.video_cache = {}

    def process_row(self, entry, row):

        # try to load marker name
        marker_id = entry.dimension[1].value
        video_id = entry.dimension[0].value

        marker_name = "Deleted"
        marker = None
        try:
            marker = Marker.objects.filter(key__iexact=marker_id).latest('modified')
        except Marker.DoesNotExist:
            try:
                marker = Marker.objects.filter(id=int(marker_id)).latest('modified')
            except Marker.DoesNotExist:
                pass
            except ValueError:
                pass

        # if there is no marker, or it is associated with the wrong video
        # return
        if not marker or marker.video_revision.video.key != video_id:
            return

        marker_id = marker.key
        marker_name = marker.title

        marker_info = {
            "total": int(entry.metric[0].value),
            "unique": int(entry.metric[1].value),
            "name": marker_name
        }

        # create entry in video cache if needed
        marker_cache = {}
        if video_id in self.video_cache:
            marker_cache = self.video_cache[video_id]
        else:
            self.video_cache[video_id] = marker_cache
        

        # if we have something in the cache, add it
        if marker_id in marker_cache:
            marker_info["total"] += marker_cache[marker_id]["total"]
            marker_info["unique"] += marker_cache[marker_id]["unique"]

        marker_cache[marker_id] = marker_info
        row.popular_markers = json.dumps(marker_cache)

#
# used by health checks to check access
#
def check_access():
    try:
        _get_client()
        return True
    except Exception as e:
        return str(e)


#
# Define which importers to use
#
importers = [
    MetricsImportPlays,
    MetricsImportMarkersClicked,
    MetricsImportSessionDuration,
    MetricsPopularMarkers,
    MetricsImportVideoCompleted,
    MetricsImportSessions
]

