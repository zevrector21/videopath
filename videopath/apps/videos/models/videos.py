from django.db import models
from django.http import Http404

class Videos(models.Manager):


	#
	# Get video for user and perform access check
	#
	def get_video_for_user(self, user, pk=None, key=None):

		if pk:
			try: 
				return self.filter_for_user(user).get(pk=pk, archived=False)
			except self.model.DoesNotExist: pass

		if key:
			try:
				return  self.filter_for_user(user).get(key=key, archived=False)
			except self.model.DoesNotExist: pass

		raise Http404


	def filter_for_user(self,user):
		return self.filter( models.Q(team__owner = user) | models.Q(team__members = user) )
