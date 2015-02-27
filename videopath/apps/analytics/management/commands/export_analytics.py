from django.core.management.base import BaseCommand

from videopath.apps.analytics.models import TotalAnalyticsData


class Command(BaseCommand):

    def handle(self, *args, **options):
        # delete tokens
        rows = []
        rows.append(["key", "Total Plays", "Unique Plays",
                     "Overlays opened", "Overlays opened unique", "Avg. Session Time"])
        for tad in TotalAnalyticsData.objects.all():
            rows.append([tad.video.key, tad.plays_all, tad.plays_unique,
                         tad.overlays_opened_all, tad.overlays_opened_unique, tad.avg_session_time])

        for row in rows:
            line = ""
            for elem in row:
                line += '"' + str(elem) + '",'
            print line
