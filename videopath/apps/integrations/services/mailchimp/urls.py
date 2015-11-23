from django.conf.urls import url, patterns, include

from .views import ListsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'list', ListsViewSet, base_name="list")

urlpatterns = patterns('',   
   url(r'', include(router.urls)),
   url(r'^beacon/', 'videopath.apps.integrations.services.mailchimp.views.beacon'),

)