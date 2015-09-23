from django.db import models
from videopath.apps.common.models import VideopathBaseModel

#
# Layout new source class
# not in use at the moment
#
class Source(VideopathBaseModel):

    # status
    STATUS_WAITING = "awaiting_upload"
    STATUS_PROCESSING = "processing"
    STATUS_OK = "ok"
    STATUS_ERROR = "error"

    STATUS_CHOICES = (
        (STATUS_WAITING, STATUS_WAITING),
        (STATUS_PROCESSING, STATUS_PROCESSING),
        (STATUS_OK, STATUS_OK),
        (STATUS_ERROR, STATUS_ERROR),
    )

    # service
    SERVICE_NONE = "none"
    SERVICE_VIDEOPATH = "videopath"
    SERVICE_YOUTUBE = "youtube"
    SERVICE_VIMEO = "vimeo"
    SERVICE_WISTIA = "wistia"
    SERVICE_BRIGHTCOVE = "brightcove"
    SERVICE_VIDEOPATH = "videopath"
    SERVICE_CUSTOM = "custom"
    SERVICE_CHOICES = (
        (SERVICE_NONE, SERVICE_NONE),
        (SERVICE_YOUTUBE, SERVICE_YOUTUBE),
        (SERVICE_VIMEO, SERVICE_VIMEO),
        (SERVICE_WISTIA, SERVICE_WISTIA),
        (SERVICE_BRIGHTCOVE, SERVICE_BRIGHTCOVE),
        (SERVICE_VIDEOPATH, SERVICE_VIDEOPATH),
        (SERVICE_CUSTOM, SERVICE_CUSTOM),
    )

    # unique id
    key = models.CharField(max_length=50, blank=True, unique=True)

    # status settings
    status = models.CharField(max_length=255, default=STATUS_OK, choices=STATUS_CHOICES)

    # service & id, such as youtube or vimeo id
    service_identifier = models.CharField(max_length=255, default="")
    service = models.CharField(max_length=255, choices=SERVICE_CHOICES, default=SERVICE_NONE)

    # media data
    duration = models.FloatField(default=0)
    aspect = models.FloatField(default=0)
    description = models.CharField(max_length=255, default="")

    # images  
    thumbnail_small = models.CharField(max_length=2048, default="")
    thumbnail_large = models.CharField(max_length=2048, default="")

    # source files (for videopath and own hosting)
    file_mp4 = models.CharField(max_length=512, default="", blank=True)
    file_webm = models.CharField(max_length=512, default="", blank=True)

    # yt special setting
    youtube_allow_clickthrough = models.BooleanField(default=False)

    # videopath
    notes = models.CharField(max_length=255, blank=True)

    # save support for jpgs
    jpg_sequence_support = models.BooleanField(default=False)
    jpg_sequence_length = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key(32)
        super(VideoSource, self).save(*args, **kwargs)