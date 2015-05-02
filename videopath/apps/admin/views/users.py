import humanize

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from videopath.apps.videos.models import Video
from videopath.apps.files.models import VideoSource
from videopath.apps.admin.views import helpers

@csrf_exempt
def listview(request):
    result = helpers.navigation()

    result += helpers.header("All Users")
    result += "Red: No videos<br />Orange: No published videos or all videos are demo videos<br />Green: Has published videos<br /><br />"
    users = []
    for u in User.objects.all():
        videos = u.videos.filter(archived=False).count()

        # published
        videos_published = u.videos.filter(published=Video.PUBLIC, archived=False).count()
        demo_videos = VideoSource.objects.filter(
            video__user=u, service_identifier="2rtGFAnyf-s").count()

        if videos == 0:
            color = "red"
        elif videos > 0 and videos_published == 0 or demo_videos == videos:
            color = "darkorange"
        else:
            color = "green"

        user = [
            "<span style = 'color:" + color + "'>" + helpers.userlink(u) + "</span>",
            "<b>" + str(videos) + "</b> videos",
            "<b>" + str(videos_published) + "</b> published",
            "<b>" + str(demo_videos) + "</b> demos"
        ]
        users.append(user)
    result += helpers.table(users)

    return HttpResponse("<pre>" + result + "</pre>")

@csrf_exempt
def listview_sales(request):
    result = helpers.navigation()

    result += helpers.header("All Users for Sales")
    users = []
    for u in User.objects.all():
        videos = u.videos.filter(archived=False).count()
        videos_published = u.videos.filter(published=Video.PUBLIC, archived=False).count()
        user = [
            "<span>" + helpers.userlink(u) + "</span>",
            "<b>" + str(videos) + "</b> videos",
            "<b>" + str(videos_published) + "</b> published",
            "<b>"+str(u.date_joined.date())+ "</b>",
            "<a target = '_blank' href='mailto:"+u.email+"'>"+u.email+"</a>",
        ]
        users.append(user)
    result += helpers.table(users)

    return HttpResponse("<pre>" + result + "</pre>")

def userview(request, username):
    result = helpers.navigation()

    # load user
    user = User.objects.get(username=username)

    result += helpers.header("User: " + username)
    result += "<a href='mailto:"+user.email+"'>" + user.email+ "</a> <br />"
    result += "Signed up " + humanize.naturaltime(user.date_joined) + "<br />"

    # last seen info
    try:
        result += "Last seen " + humanize.naturaltime(user.activity.last_seen) + "<br />"
    except:
        pass

    try:
        result += "Currently subscribed to " + user.subscription.plan
    except:
        pass

    # billing info
    result += helpers.header("Billing Adress")
    try:
        result += user.payment_details.name + "<br />"
        result += user.payment_details.street + "<br />"
        result += user.payment_details.city + "<br />"
        result += user.payment_details.post_code + "<br />"
        result += user.payment_details.country + "<br />"
    except:
        pass


    # published videos 
    result += helpers.header("Published Videos")
    videos = user.videos.filter(archived=False, published=Video.PUBLIC).order_by('-current_revision__modified')
    result += helpers.videolist(videos)

    # unpublished videos
    result += helpers.header("Unpublished Videos")
    videos = user.videos.filter(archived=False, published=Video.PRIVATE).order_by('-current_revision__modified')
    result += helpers.videolist(videos)

    # deleted projects videos
    result += helpers.header("Deleted Videos")
    videos = user.videos.filter(archived=True).order_by('-current_revision__modified')
    result += helpers.videolist(videos)


    return HttpResponse("<pre>" + result + "</pre>")
