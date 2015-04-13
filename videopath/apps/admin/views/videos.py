from datetime import timedelta, datetime, date
import humanize

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum

from videopath.apps.videos.models import Video
from videopath.apps.analytics.models import DailyAnalyticsData
from videopath.apps.admin.views import helpers


@csrf_exempt
def listview(request):
    result = helpers.navigation()

    # video plays
    result += helpers.header("Plays of videos by user in the last 7 days")
    last_day = date.today()
    first_day = last_day - timedelta(days=7)
    count = DailyAnalyticsData.objects.filter(
        # video__user=user,
        date__gte=first_day,
        date__lt=last_day)\
        .values('video__user__username')\
        .annotate(score=Sum("plays_all"))\
        .order_by('-score')
    max_rows = 7
    for entry in count:
        result += entry["video__user__username"] + \
            ": " + str(entry["score"]) + " plays<br />"
        max_rows = max_rows - 1
        if max_rows <= 0:
            break

    result += helpers.header("Most popular video the last 7 days")
    last_day = date.today()
    first_day = last_day - timedelta(days=7)
    count = DailyAnalyticsData.objects.filter(
        # video__user=user,
        date__gte=first_day,
        date__lt=last_day)\
        .values('video_id')\
        .annotate(score=Sum("plays_all"))\
        .order_by('-score')
    max_rows = 10
    for entry in count:
        video = Video.objects.get(pk=entry["video_id"])
        link = "http://player.videopath.com/" + video.key
        result += "<a href='" + link + "'>"+video.get_draft_or_current_revision().title + "</a> (" + video.user.username + ")" + \
            ": " + str(entry["score"]) + " plays<br />"
        max_rows = max_rows - 1
        if max_rows <= 0:
            break

    # videos created per week
    result += helpers.header("Videos created per week")
    result += helpers.dategraph(Video.objects.all(), "created", "%Y %V")

    # published vids
    startdate = datetime.now()
    enddate = startdate - timedelta(days=30)
    result += helpers.header("Recently published videos")
    videos = Video.objects.filter(current_revision__modified__range=[
                                  enddate, startdate]).order_by('-current_revision__modified')
    for v in videos:
        url = "http://player.videopath.com/" + v.key
        title = "<a href ='" + url + "' target = '_blank' >" + v.current_revision.title + \
            "</a> (" + v.user.username + ", " + \
            humanize.naturalday(v.current_revision.modified) + ")"
        result += title
        result += "<br />"

    return HttpResponse("<pre>" + result + "</pre>")


@csrf_exempt
def videoview(request, key):
    result = helpers.navigation()
    video = Video.objects.get(key=key)

    result += helpers.header("Video " + video.get_current_revision_or_draft().title)
    result += "User: " + helpers.userlink(video.user)

    result += helpers.header("Overall stats")
    try:
        data = video.total_analytics.latest("plays_all")

        percent_interacting = int(min(100, (float(data.overlays_opened_unique / float(data.plays_all)) * 100)))
        clicks_per_user = (float(data.overlays_opened_all) / float(data.plays_all))

        result += "Plays: " + str(data.plays_all) + "\n"
        result += "Plays unique: " + str(data.plays_unique) + "\n"
        result += "Average Session Duration: " + str(data.avg_session_time) + "\n"
        result += "Clicks on markers: " + str(data.overlays_opened_all) + "\n"
        result += "Clicks on markers unique: " + str(data.overlays_opened_unique) + "\n"
        result += "Viewers interacting: " + str(percent_interacting) + "%\n"
        result += "Average clicks per user: " + str(clicks_per_user) + "\n"

    except:
        result += "No stats available at this time"

    return HttpResponse("<pre>" + result + "</pre>")
