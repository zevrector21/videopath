from django.db import models
from django.http import Http404

class VideoManager(models.Manager):

	#
	# Get the video regardless wether a key or the id is used
	#
	def get_video_or_404(self, vid, user=None):
		try:
		    video = self.get(key=vid, archived=False)
		except self.model.DoesNotExist:
			try:
			    video = self.get(pk=str(vid), archived=False)
			except self.model.DoesNotExist:
			    raise Http404

		if user and not (video.user.id == user.id):
			raise Http404

		return video