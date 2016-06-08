from django.contrib import admin

from .base import VideopathModelAdmin

from ..models import  Video

#
# Video Admin
#
class VideoAdmin(VideopathModelAdmin):

	only_superusers = False

	list_display = ('key','created', 'player_version', 'team', 'title','total_plays')
	list_filter = ['player_version',]
	search_fields = ['draft__title', 'key', 'team__owner__username']
	ordering = ('-created',)

	def title(self,obj):
		return obj.draft.title
admin.site.register(Video, VideoAdmin)