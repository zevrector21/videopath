from django.conf.urls import url, patterns, include

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
from .views import IntegrationViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'integration', IntegrationViewSet, base_name="integration")

urlpatterns = patterns('',   
   url(r'', include(router.urls)),
)