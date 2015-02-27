import re
import simplejson
import urllib2
import requests

from videopath.apps.files.models import VideoSource

# url extractors
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


def get_service_from_url(url):
    for test in url_tests:
        for regex in url_tests[test]:
            m = re.search(regex, url)
            if m:
                return test, m.group(1)
    return False, False


def import_url(video, url):
    service, key = get_service_from_url(url)

    if service == "youtube":
        return import_youtube(video, key)
    if service == "vimeo":
        return import_vimeo(video, key)
    if service == "wistia":
        return import_wistia(video,key)
    else:
        return False, "Please double check that you copied a valid Video URL."


def convert_yt_duration_string(string):
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


def import_wistia(video, wistia_id):

    wistia_url = "http://fast.wistia.net/oembed?url=http%3A%2F%2Fhome.wistia.com%2Fmedias%2F_KEY_".replace('_KEY_', wistia_id)
    print wistia_url

    try:
        response = requests.get(wistia_url)
        item = response.json()

        source = VideoSource.objects.create(
            video=video,
            title=item["title"],
            service_identifier=wistia_id,
            status=VideoSource.STATUS_OK,
            service=VideoSource.SERVICE_WISTIA,
            video_duration=item["duration"],
            video_aspect=float(item["width"]) / float(item["height"]),
            thumbnail_url=item["thumbnail_url"]
        )

        return True, source
    except urllib2.HTTPError:
        return False, "Error"

    # all set
    return True, False


def import_vimeo(video, vimeo_id):
    # request url
    vimeo_url = "http://vimeo.com/api/v2/video/_KEY_.json".replace(
        '_KEY_', vimeo_id)
    try:
        response = urllib2.urlopen(vimeo_url)
        j = simplejson.load(response)
        item = j[0]

        source = VideoSource.objects.create(
            video=video,
            title=item["title"],
            service_identifier=vimeo_id,
            status=VideoSource.STATUS_OK,
            service=VideoSource.SERVICE_VIMEO,
            video_duration=item["duration"],
            video_aspect=float(item["width"]) / float(item["height"]),
            thumbnail_url=item["thumbnail_large"]
        )

        return True, source
    except urllib2.HTTPError:
        return False, "Error"

    # all set
    return True, False


def import_youtube(video, youtube_id):

    # build api urls
    v3_api_url = "https://www.googleapis.com/youtube/v3/videos?id=_KEY_&part=snippet,statistics,contentDetails,status&key=AIzaSyBLmIRp_0JZDxWDGl8ZkIzmwT1W1NSOfLk".replace(
        "_KEY_", youtube_id)

    try:
        response = urllib2.urlopen(v3_api_url)
        result_json = simplejson.load(response)
        item = result_json["items"][0]

        # see if we can access it
        embeddable = item["status"]["embeddable"]
        privacyStatus = item["status"]["privacyStatus"]
        if not embeddable:
            return False, "This Video is not embedabble. Please change this in your Youtube settings."
        if privacyStatus != "public" and privacyStatus != "unlisted":
            return False, "Please set your Youtube video to public. <a target = '_blank' href = 'http://videopath.com/tutorial/importing-videos-from-youtube/'>Learn more</a>."

        # get values
        duration = convert_yt_duration_string(
            item["contentDetails"]["duration"])
        title = item["snippet"]["title"]
        title = (title[:250] + '..') if len(title) > 250 else title

        try:
           video.draft.title = title
           video.draft.save()
        except:
           pass

        if duration == 0:
            return False, "There was an error retrieving the information for this video from Youtube. Please try again."

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

        # all set !
        source = VideoSource.objects.create(video=video, title=title, service_identifier=youtube_id, status=VideoSource.STATUS_OK,
                                            service=VideoSource.SERVICE_YOUTUBE, video_duration=duration, video_aspect=aspect, thumbnail_url=thumbnail_url)
        return True, source
    except:
        return False, "This doesn't look like a video URL."

    return True, False


def num(var):
    try:
      return int(float(var))
    except:
        return 0

def import_custom(video, vars):

    mp4 = vars["mp4"]
    webm = vars["webm"]
    width = num(vars["width"])
    height = num(vars["height"])
    duration = num(vars["duration"])

    # test existence of mp4 file
    try:
        resp = requests.head(mp4)
    except:
        return False, "Could not verify the existense of a mp4 file at the given location."
    if resp.status_code != 200:
        return False, "Could not find a mp4 file at the given location."

    # test existence of webm file
    try:
        resp = requests.head(webm)
    except:
        return False, "Could not verify the existense of a webm file at the given location."
    if resp.status_code != 200:
        return False, "Could not find a webm file at the given location."

    if duration <= 0:
        return False, "Invalid duration."

    if width <= 0:
        return False, "Invalid width"

    if height <= 0:
        return False, "Invalid height"

    aspect = float(width) / float(height)

    source = VideoSource.objects.create(video=video, status=VideoSource.STATUS_OK,
                                            service=VideoSource.SERVICE_CUSTOM, video_duration=duration, video_aspect=aspect, source_mp4=mp4, source_webm=webm)
    return True, source
