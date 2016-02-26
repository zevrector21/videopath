from django.db.models import Count
from django.contrib import admin
from .models import User
from videopath.apps.videos.models import Video
from urlparse import urlparse

from videopath.apps.payments.actions import start_trial

PIPEDRIVE_PERSON_URL = 'https://videopath.pipedrive.com/person/'

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
		try:
			plan = obj.subscription.plan
		except:
			return 'free-free'
		status = ''
		try:
			status = 'switches to {0} on {1}'.format(obj.pending_subscription.plan, obj.subscription.current_period_end)
		except: 	
			if obj.subscription.current_period_end:
				status = 'renews {0}'.format(obj.subscription.current_period_end)

		return "{0}<br />{1}".format(plan, status)
	plan.admin_order_field = 'subscription__plan'
	plan.allow_tags = True
    
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

	def retention_mails(self,obj):
		return obj.settings.receive_retention_emails
	retention_mails.admin_order_field ='settings__receive_retention_emails'


	def pipedrive(self,obj):
		try:
			pid = obj.sales_info.pipedrive_person_id
			return '<a href="{0}">{1}</a>'.format(PIPEDRIVE_PERSON_URL + str(pid), pid)
		except:
			return '-'
	pipedrive.allow_tags=True

	def email_link(self, obj):
		return '<a href ="/admin/insights/users/{0}/">{0}</a>'.format(obj.email)
	email_link.admin_order_field = 'email'
	email_link.allow_tags=True

	list_display = (
	        'email_link', 
	        'date_joined',
	        'country',
	        'phone',
	        'referrer',
	        'plan',
	        'videos',
	        'pipedrive',
	        'retention_mails')

	#
	# Actions
	#
	actions=["make_toggle_retention_mails", "make_trial_2_weeks", "make_trial_4_weeks"]

	def make_trial_2_weeks(self, request, queryset):
		for user in queryset.all():
			result = start_trial.run(user, 2)
			if not result: self.message_user(request, "Could not start trial. User {0} was not on the free plan!".format(user))

	make_trial_2_weeks.short_description = "2 Weeks Trial"

	def make_trial_4_weeks(self, request, queryset):
		for user in queryset.all():
			result = start_trial.run(user, 4)
			if not result: self.message_user(request, "Could not start trial. User {0} was not on the free plan!".format(user))

	make_trial_4_weeks.short_description = "4 Weeks Trial"


	def make_toggle_retention_mails(self, request, queryset):
	    for user in queryset.all():
		    user.settings.receive_retention_emails = not user.settings.receive_retention_emails
		    user.settings.save()
	make_toggle_retention_mails.short_description = "Toggle Retention mails"

	#
	# Disable delete for this list
	#
	def has_delete_permission(self, request, obj=None):
		return False
    	
	#
	# Filter & Search
	#
	search_fields = ['username', 'email']
	list_filter = ['subscription__plan', 'campaign_data__country']

	#
	# Other settings
	#
	list_select_related = ('settings', 'campaign_data')
	ordering = ('-date_joined',)
	list_display_links = None
	change_list_filter_template = "admin/filter_listing.html"

admin.site.register(User, UserAdmin)
