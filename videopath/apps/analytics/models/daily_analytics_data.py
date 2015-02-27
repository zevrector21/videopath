from django.db import models

from videopath.apps.analytics.models.base_analytics_data import BaseAnalyticsData
from videopath.apps.videos.models import Video

class DailyAnalyticsData(BaseAnalyticsData):

    video = models.ForeignKey(Video, related_name="daily_analytics")
    date = models.DateField()

    class Meta:
        app_label = "analytics"
