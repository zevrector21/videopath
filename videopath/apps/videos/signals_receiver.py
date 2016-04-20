from django.db.models.signals import post_save
from django.dispatch import receiver
from videopath.apps.vp_admin.signals import hourly_jobs

from videopath.apps.videos.models import Video, VideoRevision, Source

from videopath.apps.payments.signals import subscription_updated

from videopath.apps.videos.util import video_export_util

#
# create first draft when video is created
# videos should always have a revision initially
#
@receiver(post_save, sender=Video)
def create_first_draft(sender, instance=None, created=False, **kwargs):
    if created and instance.draft == None:
        revision = VideoRevision.objects.create(video=instance)
        instance.draft = revision
        instance.save()
        revision.save()



@receiver(hourly_jobs)
def transcode_random_video(sender, **kwargs):

	source = Source.objects.filter(jpg_sequence_support=True, sprite_support=False).order_by('?').first()
	source.export_jpg_sequence()

	source = Source.objects.filter(jpg_sequence_support=True, sprite_support=False).order_by('?').first()
	source.export_jpg_sequence()

	source = Source.objects.filter(jpg_sequence_support=True, sprite_support=False).order_by('?').first()
	source.export_jpg_sequence()

	source = Source.objects.filter(jpg_sequence_support=True, sprite_support=False).order_by('?').first()
	source.export_jpg_sequence()

@receiver(subscription_updated)
def export_users_videos(sender, user=None, **kwargs):
	video_export_util.export_user_videos(user)
	print 'done!'