from django.db.models.signals import post_save
from django.dispatch import receiver

from videopath.apps.videos.models import Video, VideoRevision

#
# create first draft when video is created
# videos should always have a revision initially
#
@receiver(post_save, sender=Video)
def create_first_draft(sender, instance=None, created=False, **kwargs):
    if created:
        revision = VideoRevision.objects.create(video=instance)
        instance.draft = revision
        instance.save()
        revision.save()
