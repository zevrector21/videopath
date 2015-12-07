from django.db import models
from django.http import Http404

class Videos(models.Manager):


	#
	# Get video for user and perform access check
	#
	def get_video_for_user(self, user, pk=None, key=None):

		if pk:
			try: 
				return self.get(pk=pk, team__owner = user, archived=False)
			except self.model.DoesNotExist: pass

		if key:
			try:
				return self.get(key=key, team__owner = user, archived=False)
			except self.model.DoesNotExist: pass

		raise Http404


	def filter_for_user(self,user):
		return self.filter( models.Q(team__owner = user) | models.Q(team__members = user) )
