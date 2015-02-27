import copy

from django.db import models

from videopath.apps.common.models import VideopathBaseModel
from videopath.apps.videos.models.video_revision import VideoRevision

class Marker(VideopathBaseModel):

    # key
    key = models.CharField(max_length=50, blank=True, db_index=True)

    # base stuff
    video_revision = models.ForeignKey(VideoRevision, related_name="markers")
    title = models.CharField(max_length=100, blank=True)
    time = models.FloatField(default=0, null=False, blank=False)

    # overlay params
    overlay_width = models.IntegerField(default=-1)
    overlay_height = models.IntegerField(default=-1)

    # duplicate the marker
    def duplicate(self):
        duplicate = copy.copy(self)
        duplicate.pk = None
        duplicate.save()

        for content in self.contents.all():
            dup_content = content.duplicate()
            dup_content.marker = duplicate
            dup_content.save()

        return duplicate

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key(8)
        super(Marker, self).save(*args, **kwargs)

    class Meta:
        app_label = "videos"

