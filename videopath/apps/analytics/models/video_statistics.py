from django.db import models

from videopath.apps.common.models import VideopathBaseModel

class VideoStatistics(VideopathBaseModel):

    # stats
    playingTotal = models.FloatField(default=0)
    overlayOpenTotal = models.FloatField(default=0)
    progressMax = models.FloatField(default=0)
    sessionTotal = models.FloatField(default=0)