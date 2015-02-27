from rest_framework import routers

from django.conf.urls import url, patterns, include

from videopath.apps.analytics.views import TotalAnalyticsDataViewSet, DailyAnalyticsDataViewSet

router = routers.DefaultRouter()
router.register(r'video/(?P<vid>[0-9]+)/analytics', TotalAnalyticsDataViewSet, base_name="analytics")
router.register(r'video/(?P<vid>[0-9]+)/analytics-daily', DailyAnalyticsDataViewSet, base_name="analytics_daily")

urlpatterns = patterns('',
	url(r'', include(router.urls))
)
