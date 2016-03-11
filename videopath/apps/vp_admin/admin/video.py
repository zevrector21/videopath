from django.contrib import admin

from .base import VideopathModelAdmin

from ..models import  Video
from ..actions import upgrade_to_player_5

#
# Video Admin
#
class VideoAdmin(VideopathModelAdmin):

	only_superusers = False

	list_display = ('key','created', 'player_version', 'team', 'title','total_plays')
	list_filter = ['player_version',]
	search_fields = ['draft__title', 'key', 'team__owner__username']
	ordering = ('-created',)

	#
	#
	#
	def make_upgrade_to_player_5(self, request, queryset):
	    for video in queryset.all():
		    result = upgrade_to_player_5.run(video)
		    if result: self.message_user(request, result)

	make_upgrade_to_player_5.short_description = "Upgrade to player 5"
	actions=["make_upgrade_to_player_5"]

	def title(self,obj):
		return obj.draft.title
admin.site.register(Video, VideoAdmin)