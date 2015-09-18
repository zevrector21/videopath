from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin

from videopath.apps.users.models import UserCampaignData, AuthenticationToken,UserActivityDay, OneTimeAuthenticationToken, UserActivity, AutomatedMail, UserSettings, User


class UserAdmin(_UserAdmin):
    list_display = (
        'pk', 'username', 'email', 'videos_link', 'date_joined', 'last_login')
    ordering = ('-date_joined',)
    search_fields = ['username', 'email']

    def videos_link(self, obj):
        link = "/admin/videos/video/?user__username=" + obj.username
        return "<a href = '" + link + "'>List of Videos</a> (" + str(obj.videos.count()) + ")"
    videos_link.allow_tags = True
    pass


class UserSettingsAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__email']


class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_seen')
    ordering = ('-last_seen',)
    

class UserActivityDayAdmin(admin.ModelAdmin):
    list_display = ('user', 'day')
    ordering = ('-day',)


class AutomatedMailAdmin(admin.ModelAdmin):
    list_display = ('user', 'mailtype', 'created')
    ordering = ('-created',)


class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created', 'last_used')
    fields = ('user',)
    ordering = ('-last_used',)


class OTTokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'created')
    #fields = ('key',)
    ordering = ('created',)

#admin.site.unregister(User)
admin.site.unregister(UserSettings)
admin.site.register(User, UserAdmin)
admin.site.register(AuthenticationToken, TokenAdmin)
admin.site.register(OneTimeAuthenticationToken, OTTokenAdmin)
admin.site.register(UserActivity, UserActivityAdmin)
admin.site.register(UserActivityDay, UserActivityDayAdmin)
admin.site.register(UserCampaignData, admin.ModelAdmin)

admin.site.register(AutomatedMail, AutomatedMailAdmin)
admin.site.register(UserSettings, UserSettingsAdmin)


