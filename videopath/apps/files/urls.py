from django.conf.urls import url, patterns


urlpatterns = patterns('',

   #
   # external notifications (for from aws)
   #
   url(r'^notifications/transcode/(?P<type>.+)/$', 'videopath.apps.files.util.transcode_notification_util.process_notification'),

   #
   # video file uploads
   #
   url(r'^video/upload/requestticket/(?P<video_id>[0-9]+)/$', 'videopath.apps.files.views.video_request_upload_ticket'),
   url(r'^video/upload/complete/(?P<ticket_id>.+)/$', 'videopath.apps.files.views.video_upload_complete'),

   #
   # image file uploads
   #
   url(r'^image/upload/requestticket/(?P<type>.+)/(?P<related_id>[0-9]+)/$', 'videopath.apps.files.views.image_request_upload_ticket'),
   url(r'^image/upload/complete/(?P<ticket_id>.+)/$', 'videopath.apps.files.views.image_upload_complete'),

   #
   # manage thumbs api
   #
   url(r'^video/thumbs/(?P<video_id>[0-9]+)/delete_custom/$', 'videopath.apps.files.views.delete_custom_thumb'), 
   url(r'^video/thumbs/(?P<video_id>[0-9]+)/$', 'videopath.apps.files.views.video_thumbs'),

   #
   # video source import
   #
   url(r'^video/(?P<key>[0-9]+)/import_source/$','videopath.apps.files.views.import_source'),
)


