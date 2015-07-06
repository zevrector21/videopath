from django.db import models

from videopath.apps.videos.models import Video, MarkerContent
from videopath.apps.common.models import VideopathBaseModel

#
# base model for all files
#
class VideopathFileBaseModel(VideopathBaseModel):
    key = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key(32)
        super(VideopathFileBaseModel, self).save(*args, **kwargs)

#
# image file for marker content
#
class ImageFile(VideopathFileBaseModel):

    # status
    CREATED = 0
    FILE_RECEIVED = 1
    PROCESSING = 2
    PROCESSED = 3
    ERROR = -1
    STATUS_CHOICES = (
        (CREATED, 'Created. Waiting for upload.'),
        (FILE_RECEIVED, 'Uploaded.'),
        (PROCESSING, 'Processing'),
        (PROCESSED, 'Processed.'),
        (ERROR, 'Error.'),
    )

    # type
    MARKER_CONTENT = "marker content"
    CUSTOM_THUMBNAIL = "custom thumbnail"
    CUSTOM_LOGO = "custom logo"
    TYPE_CHOICES = (
        (MARKER_CONTENT, 'Image for Marker Content'),
        (CUSTOM_THUMBNAIL, 'Image for custom video thumbnail'),
        (CUSTOM_LOGO, 'Image for custom logo on player chrome'),
    )

    # marker content link
    markercontent = models.ManyToManyField(
        MarkerContent, related_name="image_file", blank=True)

    #
    status = models.SmallIntegerField(default=CREATED, choices=STATUS_CHOICES)
    image_type = models.CharField(
        max_length=255, blank=True, choices=TYPE_CHOICES, default=MARKER_CONTENT)

    # image data
    width = models.SmallIntegerField(default=0)
    height = models.SmallIntegerField(default=0)

    # file info
    bytes = models.BigIntegerField(default=0)
    original_file_name = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return u'%s %s' % ("ImageFile", self.key)

#
# video source file for videos
#
class VideoFile(VideopathFileBaseModel):

    # status
    CREATED = 0
    FILE_RECEIVED = 1
    TRANSCODE_SUBMITTED = 2
    TRANSCODING_STARTED = 3
    TRANSCODING_COMPLETE = 4
    TRANSCODING_ERROR = -1
    STATUS_CHOICES = (
        (CREATED, 'Created. Waiting for upload.'),
        (FILE_RECEIVED, 'Uploaded.'),
        (TRANSCODE_SUBMITTED, 'Transcoding job submitted.'),
        (TRANSCODING_STARTED, 'Transcoding started.'),
        (TRANSCODING_COMPLETE, 'Transcoding complete.'),
        (TRANSCODING_ERROR, 'Transcoding error.'),
    )

    # video link
    video = models.ForeignKey(Video, related_name="file")

    # status
    status = models.SmallIntegerField(default=CREATED, choices=STATUS_CHOICES)

    # transcoding info
    transcoding_job_id = models.CharField(max_length=255, blank=True)
    transcoding_result = models.CharField(max_length=255, blank=True)

    # video info
    video_width = models.SmallIntegerField(default=0)
    video_height = models.SmallIntegerField(default=0)
    video_duration = models.FloatField(default=0)
    video_aspect = models.FloatField(default=0)

    # thumbnail info
    thumbnail_index = models.SmallIntegerField(default=0)
    original_file_name = models.CharField(max_length=255, blank=True)

    # size of file
    original_bytes = models.BigIntegerField(default=0)
    transcoded_bytes = models.BigIntegerField(default=0)

#
# Video source, such as youtube etc for video
#
class VideoSource(VideopathBaseModel):

    # service type
    SERVICE_NONE = "none"
    SERVICE_YOUTUBE = "youtube"
    SERVICE_VIMEO = "vimeo"
    SERVICE_WISTIA = "wistia"
    SERVICE_BRIGHTCOVE = "brightcove"
    SERVICE_CUSTOM = "custom"
    SERVICE_CHOICES = (
        (SERVICE_NONE, SERVICE_NONE),
        (SERVICE_YOUTUBE, SERVICE_YOUTUBE),
        (SERVICE_VIMEO, SERVICE_VIMEO),
        (SERVICE_WISTIA, SERVICE_WISTIA),
        (SERVICE_BRIGHTCOVE, SERVICE_BRIGHTCOVE),
        (SERVICE_CUSTOM, SERVICE_CUSTOM),
    )

    # service status
    STATUS_CREATED = 0
    STATUS_OK = 1
    STATUS_ERROR = -1
    STATUS_CHOICES = (
        (STATUS_CREATED, 'created'),
        (STATUS_OK, 'ok'),
        (STATUS_ERROR, 'error'),
    )

    # video link
    video = models.ForeignKey(
        Video, related_name="video_sources", blank=True, null=True)

    # status settings
    service = models.CharField(
        max_length=255, choices=SERVICE_CHOICES, default=SERVICE_NONE)
    status = models.SmallIntegerField(
        default=STATUS_CREATED, choices=STATUS_CHOICES)

    # identifier, such as youtube or vimeo id
    service_identifier = models.CharField(max_length=255, default="")

    # fields for hosted sources
    source_mp4 = models.CharField(max_length=512, default="", blank=True)
    source_webm = models.CharField(max_length=512, default="", blank=True)
    
    # video details
    video_duration = models.FloatField(default=0)
    video_aspect = models.FloatField(default=0)

    # video meta data
    title = models.CharField(max_length=255, default="")

    #
    thumbnail_url = models.CharField(max_length=2048, default="")

    # special settings
    allow_youtube_clickthrough = models.BooleanField(default=False)
