from django.contrib import admin

from videopath.apps.analytics.models import TotalAnalyticsData, DailyAnalyticsData

class TotalAnalyticsDataAdmin(admin.ModelAdmin):
    list_display = ('video', 'plays_all', 'plays_unique',
                    'overlays_opened_all', 'avg_session_time', 'video_completed', 'sessions')
    search_fields = ['video__id']

class DailyAnalyticsDataAdmin(admin.ModelAdmin):
    list_display = ('video', 'date', 'plays_all', 'plays_unique',
                    'overlays_opened_all', 'avg_session_time', 'video_completed', 'sessions')
    ordering = ('-date',)
    search_fields = ['video__id']

admin.site.register(TotalAnalyticsData, TotalAnalyticsDataAdmin)
admin.site.register(DailyAnalyticsData, DailyAnalyticsDataAdmin)
