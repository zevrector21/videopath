from django.conf.urls import url, patterns, include

from rest_framework import routers

from videopath.apps.videos.views import MarkerViewSet, MarkerContentViewSet, VideoViewSet, VideoRevisionViewSet
from videopath.apps.videos.views import video_publish, get_revision, send_share_mail
from videopath.apps.videos.views import icon_view, thumbnail_view

# Register view sets
router = routers.DefaultRouter()
router.register(r'video/(?P<vid>[0-9]+)/revision', VideoRevisionViewSet, base_name="video_revision")
router.register(r'video-revision/(?P<vid>[0-9]+)/marker', MarkerViewSet, base_name="marker")
router.register(r'marker/(?P<mid>[0-9]+)/content', MarkerContentViewSet, base_name="marker_content")

router.register(r'marker', MarkerViewSet, base_name="marker")
router.register(r'video', VideoViewSet, base_name="video")
router.register(r'video-revision', VideoRevisionViewSet, base_name="video_revision")
router.register(r'markercontent', MarkerContentViewSet, base_name="marker_content")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',   

   # special urls that overwrite the Viewsets
   url(r'^video/(?P<vid>[0-9]+)/revision/(?P<rev_type>draft|published)/$', get_revision),

   # publish / unpublish actions
   url(r'^video/(?P<vid>[0-9]+)/public/$', video_publish),

   # send share email
   url(r'^video/(?P<vid>[0-9]+)/share-email/$', send_share_mail),

   # file uploads, icon and thumbnail respectively
   url(r'^video-revision/(?P<rid>[0-9]+)/icon', icon_view),
   url(r'^video-revision/(?P<rid>[0-9]+)/thumbnail', thumbnail_view),

   # regular api urls
   url(r'', include(router.urls)),
)