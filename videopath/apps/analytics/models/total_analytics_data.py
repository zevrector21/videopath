from django.db import models

from videopath.apps.analytics.models.base_analytics_data import BaseAnalyticsData
from videopath.apps.videos.models import Video

class TotalAnalyticsData(BaseAnalyticsData):

    video = models.ForeignKey(Video, related_name="total_analytics")
    
    class Meta:
        app_label = "analytics"