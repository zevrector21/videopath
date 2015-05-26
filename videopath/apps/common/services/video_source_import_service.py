import re
import simplejson
import urllib2
import requests



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
    else:
        _raise("Please double check that you copied a valid Video URL.")

def _get_service_from_url(url):
    for test in url_tests:
        for regex in url_tests[test]:
            m = re.search(regex, url)
            if m:
                return test, m.group(1)
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
    ]
}

#
# Youtube Imports
#
def _import_youtube(key):

    # build api urls
    v3_api_url = "https://www.googleapis.com/youtube/v3/videos?id=_KEY_&part=snippet,statistics,contentDetails,status&key=AIzaSyBLmIRp_0JZDxWDGl8ZkIzmwT1W1NSOfLk".replace(
        "_KEY_", key)

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
    
    return {
    	"title": title,
    	"service_identifier": key,
    	"service": "youtube",
    	"video_duration": duration,
    	"video_aspect": aspect,
    	"thumbnail_url": thumbnail_url
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
            "title":item["title"],
            "service_identifier":key,
            "service":"vimeo",
            "video_duration":item["duration"],
            "video_aspect":float(item["width"]) / float(item["height"]),
            "thumbnail_url":item["thumbnail_large"]
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
            "title":item["title"],
            "service_identifier":key,
            "service":"wistia",
            "video_duration":item["duration"],
            "video_aspect":float(item["width"]) / float(item["height"]),
            "thumbnail_url":item["thumbnail_url"]
        }
    except urllib2.HTTPError:
        _raise()

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
		"video_duration": duration,
		"video_aspect": aspect,
		"source_mp4": mp4,
		"source_webm": webm
	}



