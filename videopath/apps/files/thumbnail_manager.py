import math

from django.conf import settings

from videopath.apps.files.video_helper import current_file_for_video
from videopath.apps.files.conf import image_conf

class ThumbnailManager():

    thumbnail_interval = 60

    # manage rendered thumbs
    def current_thumbnail_index_for_video(self, v):
        file = current_file_for_video(v)
        if file is None:
            return -1
        if v == None or file == None:
            return -1
        max = self.thumbnail_count_for_video(v)
        if file.thumbnail_index > max or file.thumbnail_index <= 0:
            if file.video_duration > (ThumbnailManager.thumbnail_interval / 2):
                return 2
            return 1
        return file.thumbnail_index

    def available_thumbs_for_video(self, v):
        result = []
        for i in range(self.thumbnail_count_for_video(v)):
            result.append(self.thumbnail_url_for_video(v, i + 1))
        return result

    def thumbnail_count_for_video(self, v):
        amount = 1
        file = current_file_for_video(v)
        duration = file.video_duration
        if duration > 30:
            amount += 1
            duration -= 30
        amount += math.floor(duration / ThumbnailManager.thumbnail_interval)
        return int(amount)

    def thumbnail_url_for_video(self, v, number=-1):
        vfile = current_file_for_video(v)
        return self.thumbnail_url_for_videofile(vfile, number)

    def thumbnail_url_for_videofile(self, vfile, number=-1):
        if vfile is None:
            return ""
        if number == -1:
            number = self.current_thumbnail_index_for_video(vfile.video)
        filename = str(number).zfill(5)
        filename = settings.THUMBNAIL_CDN + vfile.key + "/" + filename + ".jpg"
        return filename

    def large_thumbnail_url_for_videofile(self, vfile, number=-1):
        if vfile is None:
            return ""
        if number == -1:
            number = self.current_thumbnail_index_for_video(vfile.video)
        filename = str(number).zfill(5)
        filename = settings.THUMBNAIL_CDN + \
            vfile.key + "/" + filename + "-hd.jpg"
        return filename

    def set_thumbnail_index_for_video(self, v, index):
        file = current_file_for_video(v)
        file.thumbnail_index = index
        file.save()

    # get thumb
    # helpers

    def thumbnails_for_video(self, video):
        return self.thumbnails_for_revision(video.current_revision)

    def thumbnails_for_revision(self, revision):

        # try custom thumbnail
        try:
            conf = image_conf[revision.custom_thumbnail.image_type]
            result = {}
            for out in conf["outs"]:
                result[out["name"]] = settings.IMAGE_CDN + \
                    out["key"].replace(
                        "_FILEKEY_", revision.custom_thumbnail.key)
            return result
        except:
            pass

        # try video source
        try:
            return {
                "normal": revision.video.video_sources.all()[0].thumbnail_url,
                "large": revision.video.video_sources.all()[0].thumbnail_url
            }
        except:
            pass

        # try video file
        try:
            videofile = revision.video.file.all()[0]
            return {
                "normal": self.thumbnail_url_for_videofile(videofile),
                "large": self.large_thumbnail_url_for_videofile(videofile)
            }
        except:
            pass

        return {
                "normal": "",
                "large": ""
            }
