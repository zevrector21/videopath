import collections
import humanize

from django.contrib.auth.models import User


base = "/admin/insights/"

company_accounts = [
        "david",
        "product_demo", #company
        "marketing", # company
        "anna",
        "tim t", #tim 2
        "tim", # tim 1
        "trival", # thomas
        "nimaa", 
        "lcdenison", # louisa 1
        "dontdelete", # louisa 2
        "yana",
        "jolly",
        "junayd",
        "vp_test_basic",
        "vp_test_pro",
        "vp_test_enterprise",
]

def header(text):
    return "<h3>" + text + "</h3>"

def table(array, header = None):
    
    result = ""
    if header:
        result = "<tr>"
        for item in header:
            result += "<th>" + item + "</th>"
        result += "</tr>"

    for row in array:
        rowr = "<tr>"
        for item in row:
            rowr += "<td>" + item + "</td>"
        result += rowr + "</tr>"

    return "<table>" + result + "</table>"

def smart_truncate(content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix

def videolink(v):
    detail_url = base + "videos/" + v.key + "/"
    revision = None
    try:
        revision = v.draft
    except:
        pass

    try:
        revision = v.current_revision
    except:
        pass

    if not revision:
        return None

    return [
        "<a href ='" + detail_url + "'>" + smart_truncate(revision.title, 50) + "</a>",
        v.user.username,
        humanize.naturalday(revision.modified),
        str(v.total_plays) 
    ] 

def videolist(videos):
    result_array = []
    for video in videos:
        link = videolink(video)
        if link:
            result_array.append(link)
    return table(result_array, ["Title", "User", "Modified", "Plays"])


def userlink(user):
    username = user.username if isinstance(user, User) else user
    url = base + 'users/' + username +"/"
    return "<a href = '"+url+"'>"+username+"</a>"




def printgraph(values, maxlength=30.0):
    result_array = []
    maxval = max(values.values())
    ratio = maxlength / maxval

    orderedvalues = collections.OrderedDict(sorted(values.items()))
    for k in orderedvalues:
        length = ratio * orderedvalues[k]
        xs = "<b>" + str(orderedvalues[k]) + "</b> "
        while length > 0:
            xs += "X"
            length -= 1
        result_array.append([k, xs])
    return table(result_array)


def dategraph(models, datefield, timeselector="%y %m"):

    values = {}
    for model in models:
        value = getattr(model, datefield)
        key = value.strftime(timeselector)
        values[key] = values.get(key, 0) + 1
    return printgraph(values)