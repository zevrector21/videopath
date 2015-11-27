import collections
import humanize

from django.contrib.auth.models import User
from django.utils.encoding import smart_text

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
            result += "<th>" + smart_text(item) + "</th>"
        result += "</tr>"

    for row in array:
        rowr = "<tr>"
        for item in row:
            rowr += "<td>" +smart_text(item) + "</td>"
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

    result = ""
    max_value = float(max(values.values()))
    count = len(values)
    width = 100.0 / float(count)

    result = reduce(lambda x, item: x + "<div class ='vp_graph_item' style='width:{0}%'><div class = 'vp_graph_label_top'>{2}</div><div class = 'vp_graph_label_bottom'>{3}</div><div class = 'vp_graph_item_inner' style='height:{1}%'></div></div>".format(width, float(values[item]) / max_value * 100, values[item], item), values, '')

    return "<div class='vp_graph'>" + result + "</div>"


groupings = {
    
}

def dategraph(models, datefield, accumulate=False):

    # build dict
    values = {}
    for model in models:
        value = getattr(model, datefield)
        key = value.strftime("week %Y %V")
        values[key] = values.get(key, 0) + 1

    # fill in empty fields
    for year in range(2014,2016):
        for week in range(1,53):
            key = "week {0} {num:02d}".format(year, num=week)
            print key
            values[key] = values.get(key, 0)

    # sort
    values = collections.OrderedDict(sorted(values.items()))

    # accumulate if needed
    if accumulate:
        total = 0
        for key in values:
            total = total + values[key]
            values[key] = total

    return printgraph(values)