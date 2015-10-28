import re
import simplejson
import urllib2
import requests
import json


#
# Import
#
def import_video_from_url( url):
    service, key = _get_service_from_url(url)
    if service == "youtube":
        return _import_youtube(key)
    if service == "vimeo":
        return _import_vimeo(key)
    if service == "wistia":
        return _import_wistia(key)
    if service == "brightcove":
        return _import_brightcove(key)
    else:
        _raise("Please double check that you copied a valid Video URL.")

def _get_service_from_url(url):
    for test in url_tests:
        for regex in url_tests[test]:
            m = re.search(regex, url)
            if m:
                groupscount = len(m.groups())
                if groupscount == 1:
                    return test, m.group(1)
                else:
                    return test, m.groups()
    return False, False


def _raise(messages = "There was an error importing this video."):
        raise Exception(messages)

#
# Imports
#
url_tests = {
    "vimeo": [
        "vimeo\.com\/([0-9]*)"
    ],
    "youtube": [
        "youtube\.com[^+]*([\w-]{11})",
        "youtu\.be[^+]*([\w-]{11})"
    ],
    "wistia": [
        "wistia.com/medias/([\w-]{8,})"
    ],
    "brightcove": [
        'brightcove.net\/([0-9]*)\/([0-9a-z\-]*)_([0-9a-z\-]*)\/index.html\?videoId=([0-9]*)'
    ]
}

#
# Youtube Imports
#
def _import_youtube(key):

    # build api urls
    v3_api_url = "https://www.googleapis.com/youtube/v3/videos?id=_KEY_&part=snippet,statistics,contentDetails,status&key=AIzaSyBLmIRp_0JZDxWDGl8ZkIzmwT1W1NSOfLk".replace(
        "_KEY_", key)
    oembed_url = "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=_KEY_&format=json".replace("_KEY_", key)

    try:
        response = urllib2.urlopen(v3_api_url)
        result_json = simplejson.load(response)
        item = result_json["items"][0]
    except:
        _raise()

    # see if we can access it
    embeddable = item["status"]["embeddable"]
    privacyStatus = item["status"]["privacyStatus"]
    if not embeddable:
        _raise("This Video is not embedabble. Please change this in your Youtube settings.")
    if privacyStatus != "public" and privacyStatus != "unlisted":
        _raise("Please set your Youtube video to public. <a target = '_blank' href = 'http://videopath.com/tutorial/importing-videos-from-youtube/'>Learn more</a>.")

    # get values
    duration = _convert_yt_duration_string(item["contentDetails"]["duration"])
    title = item["snippet"]["title"]
    title = (title[:250] + '..') if len(title) > 250 else title

    if duration == 0:
        _raise("There was an error retrieving the information for this video from Youtube. Please try again.")

    # get largest thumbnail
    max_width = 0
    max_height = 0
    thumbnail_url = ""
    for thumb in item["snippet"]["thumbnails"].values():
        if thumb["width"] > max_width:
            max_width = thumb["width"]
            max_height = thumb["height"]
            thumbnail_url = thumb["url"]

    aspect = float(max_width) / float(max_height)

    # try hitting the oembed url and getting more correct video dimensions
    try:
        response = urllib2.urlopen(oembed_url)
        result_json = simplejson.load(response)
        aspect = float(result_json['width']) / float(result_json['height'])
        print aspect
    except:
        pass
    
    return {
    	"description": title,
    	"service_identifier": key,
    	"service": "youtube",
    	"duration": duration,
    	"aspect": aspect,
    	"thumbnail_small": thumbnail_url,
        "thumbnail_large": thumbnail_url
    }


def _convert_yt_duration_string(string):
    result = 0
    # secs
    m = re.search("([0-9]*)S", string)
    if m:
        result += int(m.group(1))
    # minutes
    m = re.search("([0-9]*)M", string)
    if m:
        result += int(m.group(1)) * 60
    # hrs
    m = re.search("([0-9]*)H", string)
    if m:
        result += int(m.group(1)) * 60 * 60
    return result

#
# Vimeo Imports
#
def _import_vimeo(key):
    # request url
    vimeo_url = "http://vimeo.com/api/v2/video/_KEY_.json".replace('_KEY_', key)
    try:
        response = urllib2.urlopen(vimeo_url)
        j = simplejson.load(response)
        item = j[0]
        return {
            "description":item["title"],
            "service_identifier":key,
            "service":"vimeo",
            "duration":item["duration"],
            "aspect":float(item["width"]) / float(item["height"]),
            "thumbnail_small":item["thumbnail_large"],
            "thumbnail_large":item["thumbnail_large"]
        }
    except urllib2.HTTPError:
        _raise()

#
# Wistia Imports
#
def _import_wistia(key):

    wistia_url = "http://fast.wistia.net/oembed?url=http%3A%2F%2Fhome.wistia.com%2Fmedias%2F_KEY_".replace('_KEY_', key)

    try:
        response = requests.get(wistia_url)
        item = response.json()
        return {
            "description":item["title"],
            "service_identifier":key,
            "service":"wistia",
            "duration":item["duration"],
            "aspect":float(item["width"]) / float(item["height"]),
            "thumbnail_small":item["thumbnail_url"],
            "thumbnail_large":item["thumbnail_url"]
        }
    except urllib2.HTTPError:
        _raise()

#
# Brightcove Imports
#
def _import_brightcove(key):

    # const
    player_url = "http://players.brightcove.net/{0}/{1}_default/index.html?videoId={2}"
    api_url = 'https://edge.api.brightcove.com/playback/v1/accounts/{0}/videos/{1}'
    re_policy_key = 'policyKey:"([A-Za-z0-9-_]*)"'

    # extract base info
    account = key[0]
    video_id = key[3]
    player = key[1]

    # get policy key by parsing player result
    player_url = player_url.format(account, player, video_id)
    response = requests.get(player_url)
    m = re.search(re_policy_key, response.text)
    policy_key = m.group(1)

   # fish out video defintions
    url = api_url.format(account, video_id)
    headers = {"BCOV-Policy":policy_key}
    response = requests.get(url, headers=headers)
    json_data = response.json()
    source = json_data["sources"][0]

    thumbnail_url = json_data["poster"]
    duration = json_data["duration"]
    width = source["width"]
    height = source["height"]

    result = {
        "service":"brightcove",
        "service_identifier":json.dumps({
            'account': str(account),
            'video_id': str(video_id),
            'player': str(player)
        }),
        "duration": duration / 1000.0,
        "aspect": float(width) / float(height),
        "thumbnail_small": thumbnail_url,
        "thumbnail_large": thumbnail_url

    }

    return result



#
# Custom Imports, if self hosting
#
def import_video_from_server(vars):

	def num(var):
	    try:
	      return int(float(var))
	    except:
	        return 0

	mp4 = vars["mp4"]
	webm = vars["webm"]
	width = num(vars["width"])
	height = num(vars["height"])
	duration = num(vars["duration"])

	# test existence of mp4 file
	try:
	    resp = requests.head(mp4)
	except:
	    _raise("Could not verify the existense of a mp4 file at the given location.")
	if resp.status_code != 200:
	    _raise("Could not find a mp4 file at the given location.")

	# test existence of webm file
	try:
	    resp = requests.head(webm)
	except:
	    _raise("Could not verify the existense of a webm file at the given location.")
	if resp.status_code != 200:
	    _raise("Could not find a webm file at the given location.")

	if duration <= 0:
	    _raise("Invalid duration.")

	if width <= 0:
	    _raise("Invalid width")

	if height <= 0:
	    _raise("Invalid height")

	aspect = float(width) / float(height)

	return {
		"service":"custom",
		"duration": duration,
		"aspect": aspect,
		"file_mp4": mp4,
		"file_webm": webm
	}



