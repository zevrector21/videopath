from datetime import timedelta, date
import humanize

from django.template.response import SimpleTemplateResponse

from django.contrib.auth.models import User
from .decorators import group_membership_required

from videopath.apps.users.models import UserActivityDay
from videopath.apps.vp_admin.views import helpers


@group_membership_required('insights')
def view(request):
    result = ""

    # activity
    enddate = date.today() - timedelta(days=30)
    daily_data = UserActivityDay.objects.filter(day__gt=enddate)

    userlist = {}
    for data in daily_data:
        if data.day == data.user.date_joined.date():
            continue
        username = data.user.username
        if not username in userlist:
            userlist[username] = [username, 0]
        userlist[username][1]+=1

    userlist = userlist.values()
    userlist.sort(key=lambda x: -x[1])
    userlist = map(lambda x: [helpers.userlink(x[0]), str(x[1]) + " days"], userlist)

    result += helpers.header("Users seen in last 30 days")
    result += "Users seen on the same day as they signed up are stripped out<br /> <br />"
    result += helpers.table(userlist)

    # signups
    enddate = date.today() - timedelta(days=7)
    users = User.objects.filter(
        date_joined__gt=enddate).order_by('-date_joined')

    result += helpers.header("Signups in last 7 days")
    userlist = []
    for user in users:
        userlist.append([
            helpers.userlink(user),
            humanize.naturaltime(user.date_joined)
        ])
    result += helpers.table(userlist)

    return SimpleTemplateResponse("insights/base.html", {
        "title": "User statistics",
        "insight_content": result
        })
