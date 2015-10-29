from datetime import timedelta, datetime, date

from django.template.response import SimpleTemplateResponse
from django.db.models import Sum
from .decorators import group_membership_required

from videopath.apps.videos.models import Video
from videopath.apps.analytics.models import DailyAnalyticsData
from videopath.apps.vp_admin.views import helpers


@group_membership_required('insights')
def listview(request):

    # video plays
    result = helpers.header("Plays of videos by user in the last 7 days")
    last_day = date.today()
    first_day = last_day - timedelta(days=7)
    count = DailyAnalyticsData.objects.filter(
        # video__user=user,
        date__gte=first_day,
        date__lt=last_day)\
        .values('video__user__username')\
        .annotate(score=Sum("plays_all"))\
        .order_by('-score')

    rows = 0
    result_array = []
    for entry in count:
        result_array.append([
                entry["video__user__username"],
                str(entry["score"])
            ])
        rows += 1
        if rows > 7:
            break
    result += helpers.table(result_array, ["username", "plays"])


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
    videos = []
    max_rows = 25
    for entry in count:
        videos.append(Video.objects.get(pk=entry["video_id"]))
        max_rows = max_rows - 1
        if max_rows <= 0:
            break
    result += helpers.videolist(videos)

    # videos created per week
    result += helpers.header("Videos created per week")
    result += "Excludes videos created by staff. <br /><br />"
    result += helpers.dategraph(Video.objects.all().exclude(user__username__in=helpers.company_accounts), "created", "%Y %V")

    # videos published per week
    result += helpers.header("Videos published per week")
    result += "Excludes videos created by staff. <br /><br />"
    result += helpers.dategraph(Video.objects.filter(published=1).exclude(user__username__in=helpers.company_accounts), "created", "%Y %V")

    # published vids
    startdate = datetime.now()
    enddate = startdate - timedelta(days=30)
    result += helpers.header("Recently published videos")
    videos = Video.objects.filter(current_revision__modified__range=[
                                  enddate, startdate]).order_by('-current_revision__modified')
    result += helpers.videolist(videos) 

    return SimpleTemplateResponse("insights/base.html", {
        "title": "Videos",
        "insight_content": result
        })



@group_membership_required('insights')
def videoview(request, key):
    video = Video.objects.get(key=key)

    result = helpers.header("General Info")
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

    result += helpers.header("Video")
    result += '<iframe width="700px" height="525px" frameborder="0" src="https://player.videopath.com/' + video.key + '" allowfullscreen="" onmousewheel="event.preventDefault();"></iframe>'

    return SimpleTemplateResponse("insights/base.html", {
        "title": "Video '" + video.get_current_revision_or_draft().title + "'",
        "insight_content": result
        })
