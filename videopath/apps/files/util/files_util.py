from django.conf import settings

from videopath.apps.files.models import ImageFile

def current_file_for_video(video):
    try:
        return video.file.latest("created")
    except:
        return None

def file_url_for_markercontent(content):
    try:
        file = content.image_file.latest("created")
        if file.status == ImageFile.PROCESSED:
            return settings.IMAGE_CDN + file.key
        return ""
    except:
        return ""