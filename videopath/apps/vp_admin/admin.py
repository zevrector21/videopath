from django.db.models import Count
from django.contrib import admin
from .models import User
from videopath.apps.videos.models import Video
from urlparse import urlparse

#
# Sales user
#
class UserAdmin(admin.ModelAdmin):

	#
	# Query set
	#
	def get_queryset(self, request):
		return User.objects.annotate(videos_count=Count('owned_teams__videos'))

	#
	# List display
	#
	def plan(self, obj):
		return obj.subscription.plan
	plan.admin_order_field = 'subscription__plan'
    
	def country(self, obj):
		return obj.campaign_data.country
	country.admin_order_field = 'campaign_data__country'

	def phone(self,obj):
		return obj.settings.phone_number

	def videos(self,obj):
		unpublished = Video.objects.filter(team__owner=obj, archived=False, published=False).count() 
		archived = Video.objects.filter(team__owner=obj, archived=True).count() 
		published = Video.objects.filter(team__owner=obj, archived=False, published=True).count() 
		return 'tot:' + str(obj.videos_count) + ' pub:' + str(published) + ' unp:' + str(unpublished) + ' arch:' + str(archived)
	videos.admin_order_field ='videos_count'

	def referrer(self,obj):
		url = obj.campaign_data.referrer
		if url:
		    parsed_uri = urlparse( url )
		    return '<a href="' + url + '">' + parsed_uri.netloc +'</a><br />';
		return ''
	referrer.allow_tags=True
	
	list_display = (
	        'email', 
	        'date_joined',
	        'country',
	        'phone',
	        'referrer',
	        'plan',
	        'videos')

	search_fields = ['username', 'email']

	list_filter = ['subscription__plan']

	# disable actions
	actions = None

admin.site.register(User, UserAdmin)
