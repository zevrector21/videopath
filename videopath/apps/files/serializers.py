from django.conf import settings

from rest_framework import serializers

from videopath.apps.files.models import VideoFile, VideoSource, ImageFile
from videopath.apps.files.util import thumbnails_util
from videopath.apps.files.settings import image_sizes



#
#
#
class VideoSourceSerializer(serializers.ModelSerializer):

    large_thumbnail_url = serializers.ReadOnlyField(source='thumbnail_url')

    class Meta:
        model = VideoSource
        fields = ('status', 'service', 'service_identifier', 'video_duration',
                  'video_aspect', 'thumbnail_url', 'large_thumbnail_url', 'source_webm', 'source_mp4')


#
#
#
class VideoFileSerializer(serializers.ModelSerializer):

    base_url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()
    video_aspect = serializers.SerializerMethodField()
    large_thumbnail_url = serializers.SerializerMethodField()

    def get_thumbnail_url(self, videofile):
        return thumbnails_util.thumbnail_url_for_videofile(videofile)

    def get_large_thumbnail_url(self, videofile):
        return thumbnails_util.large_thumbnail_url_for_videofile(videofile)

    def get_base_url(self, videofile):
        return settings.VIDEO_CDN + videofile.key

    def get_video_aspect(self, videofile, *args, **kwargs):
        if videofile.video_height == 0:
            return 0
        return float(videofile.video_width) / float(videofile.video_height)

    class Meta:
        model = VideoFile
        fields = ('status', 'video_aspect', 'video_duration',
                  'thumbnail_url', 'status', 'base_url', 'large_thumbnail_url')

#
#
#
class ImageFileSerializer(serializers.ModelSerializer):

    representations = serializers.SerializerMethodField()

    def get_representations(self, imagefile):
        conf = image_sizes[imagefile.image_type]
        result = {}
        for out in conf["outs"]:
            result[out["name"]] = settings.IMAGE_CDN + \
                out["key"].replace("_FILEKEY_", imagefile.key)
        return result

    class Meta:
        model = ImageFile
        fields = ('status', 'representations')
