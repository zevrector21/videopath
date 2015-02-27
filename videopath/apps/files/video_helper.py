from django.conf import settings

from videopath.apps.files.models import ImageFile

def current_file_for_video(video):
    try:
        return video.file.latest("created")
    except:
        return None


def thumbnail_url_for_video(video):
    vfile = current_file_for_video(video)
    if vfile is None:
        return ""
    suffix = "/00002.jpg" if vfile.video_duration > 30 else "/00001.jpg"
    return settings.THUMBNAIL_CDN + vfile.key + suffix


def file_base_url_for_video(video):
    try:
        return settings.VIDEO_CDN + current_file_for_video(video).key
    except:
        return ""


def file_state_for_video(video):
    try:
        return current_file_for_video(video).status
    except:
        return 0


def file_url_for_markercontent(content):
    try:
        file = content.image_file.latest("created")
        if file.status == ImageFile.PROCESSED:
            return settings.IMAGE_CDN + file.key
        return ""
    except:
        return ""


def file_duration_for_video(video):
    try:
        return current_file_for_video(video).video_duration
    except:
        return 0
