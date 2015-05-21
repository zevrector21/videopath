from django.conf.urls import url, patterns

notification_handler = 'videopath.apps.files.util.transcode_notification_util.process_notification'

urlpatterns = patterns('',

   # external notifications (for from aws)
   url(r'^notifications/transcode/complete/$', notification_handler, {'notification_type': 'complete'}),
   url(r'^notifications/transcode/error/$', notification_handler, {'notification_type': 'error'}),
   url(r'^notifications/transcode/progressing/$', notification_handler, {'notification_type': 'progressing'}),

   # legacy, should be removed when app is migrated (???)
   url(r'^video/upload/requestticket/(?P<video_id>[0-9]+)/$', 'videopath.apps.files.views.video_request_upload_ticket'),
   url(r'^video/upload/complete/(?P<ticket_id>.+)/$', 'videopath.apps.files.views.video_upload_complete'),
   url(r'^image/upload/requestticket/(?P<content_id>[0-9]+)/$','videopath.apps.files.views.image_request_upload_ticket_legacy'),

   # should probably somehow be converted to a post / put thing
   url(r'^image/upload/requestticket/(?P<type>.+)/(?P<related_id>[0-9]+)/$', 'videopath.apps.files.views.image_request_upload_ticket'),
   url(r'^image/upload/complete/(?P<ticket_id>.+)/$', 'videopath.apps.files.views.image_upload_complete'),

   # manage thumbs api
   url(r'^video/thumbs/(?P<video_id>[0-9]+)/delete_custom/$', 'videopath.apps.files.views.delete_custom_thumb'), 
   url(r'^video/thumbs/(?P<video_id>[0-9]+)/$', 'videopath.apps.files.views.video_thumbs'),

   # should be a post on video or revision object
   url(r'^video/(?P<key>[0-9]+)/import_source/$','videopath.apps.files.views.import_source'),
)


