from django.conf.urls import url, patterns

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.

from .oauth_views import oauth_receive

urlpatterns = patterns('',   

   # oauth endpoint
   url(r'^receive/(?P<service>mailchimp)/(?P<uid>[0-9]+)/$', oauth_receive),

)