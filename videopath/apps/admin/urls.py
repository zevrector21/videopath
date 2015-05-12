from django.conf.urls import url, patterns

urlpatterns = patterns('',
   url(r'^insights/kpis/', 'videopath.apps.admin.views.kpis.view'),

   url(r'^insights/users/sales/', 'videopath.apps.admin.views.users.listview_sales'),
   url(r'^insights/users/(?P<username>.+)/', 'videopath.apps.admin.views.users.userview'),
   url(r'^insights/users/', 'videopath.apps.admin.views.users.listview'),

   url(r'^insights/subscriptions/', 'videopath.apps.admin.views.subscriptions.view'),

   url(r'^insights/userstats/', 'videopath.apps.admin.views.userstats.view'),
   
   url(r'^insights/videos/(?P<key>.+)/', 'videopath.apps.admin.views.videos.videoview'),
   url(r'^insights/videos/', 'videopath.apps.admin.views.videos.listview'),

   url(r'^insights/billing/', 'videopath.apps.admin.views.billing.view'),
   url(r'^insights/', 'videopath.apps.admin.views.base.view'),

   # url for external health check
   url(r'^YT58Pc3u6ZlK/health/', 'videopath.apps.admin.views.health_check.view'),
   )


#from django.contrib.admin.views.decorators import staff_member_required
