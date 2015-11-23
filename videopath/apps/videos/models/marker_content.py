import copy

from django.db import models

from videopath.apps.common.models import VideopathBaseModel
from videopath.apps.videos.models.marker import Marker

class MarkerContent(VideopathBaseModel):
    TYPE_CHOICES = (
        ("text", "text"),
        ("title", "title"),
        ("image", "image"),
        ("website", "website"),
        ("map", "map"),
        ("video", "video"),
        ("media", "media"),
        ("audio", "audio"),
        ("simple_button", "simple_button"),
        ("social", "social"),
        ("email_collector", "email_collector")
    )

    # key
    key = models.CharField(max_length=50, blank=True, db_index=True)
    
    marker = models.ForeignKey(Marker, related_name='contents')
    type = models.CharField(
        max_length=20, choices=TYPE_CHOICES, default="text")
    ordinal = models.IntegerField(null=True, blank=True, default=0)

    text = models.TextField(null=True, blank=True)
    data = models.TextField(null=True, blank=True)

    title = models.CharField(max_length=255, blank=True)

    url = models.CharField(max_length=255, blank=True)

    # duplicate the marker content
    def duplicate(self):
        duplicate = copy.copy(self)
        duplicate.pk = None
        duplicate.save()

        # special case file handling
        duplicate.image_file.add(*self.image_file.all())
        duplicate.save()

        return duplicate

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key(8)
        super(MarkerContent, self).save(*args, **kwargs)

    class Meta:
        app_label = "videos"
