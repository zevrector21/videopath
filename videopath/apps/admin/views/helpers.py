import collections
import humanize

from django.contrib.auth.models import User


base = "/admin/YT58Pc3u6ZlK/insights/"


def navigation():
    result = ""
    result += "<a href='"+base+"'>Main</a> | "
    result += "<a href='"+base+"kpis/'>KPIs</a> | "
    result += "<a href='"+base+"userstats/'>Userstats</a> | "
    result += "<a href='"+base+"users/'>Userlist</a> | "
    result += "<a href='"+base+"videos/'>Videos</a>"
    return result

def header(text):
    return "<br /><br /><h3>" + text + "</h3>"

def videolink(v):
    url = "http://player.videopath.com/" + v.key
    revision = None
    try:
        revision = v.draft
    except:
        raise
        pass

    try:
        revision = v.current_revision
    except:
        pass

    if not revision:
        return None

    title = "<a href ='" + url + "' target = '_blank' >" + revision.title + \
        "</a> (" + v.user.username + ", " + \
        humanize.naturalday(revision.modified) + ", "+ \
        str(v.total_plays) + " plays)"
    return title

def videolist(videos):
    result = ""
    for video in videos:
        link = videolink(video)
        if link is None:
            continue
        result += link + "<br />"
    return result

def userlink(user):
    username = user.username if isinstance(user, User) else user
    url = base + 'users/' + username +"/"
    return "<a href = '"+url+"'>"+username+"</a>"

def table(array):
    result = ""
    for row in array:
        rowr = "<tr>"
        for item in row:
            rowr += "<td>" + item + "</td>"
        result += rowr + "</tr>"

    return "<table>" + result + "</table>"


def printgraph(values, maxlength=30.0):
    result = ""
    maxval = max(values.values())
    ratio = maxlength / maxval

    orderedvalues = collections.OrderedDict(sorted(values.items()))
    for k in orderedvalues:
        length = ratio * orderedvalues[k]
        result += k + "\t"
        while length > 0:
            result += "X"
            length -= 1
        result += " " + str(orderedvalues[k]) + " <br />"
    return result


def dategraph(models, datefield, timeselector="%y %m"):

    values = {}
    for model in models:
        value = getattr(model, datefield)
        key = value.strftime(timeselector)
        values[key] = values.get(key, 0) + 1
    return printgraph(values)