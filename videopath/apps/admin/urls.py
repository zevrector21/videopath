from django.conf.urls import url, patterns

urlpatterns = patterns('',
   url(r'^YT58Pc3u6ZlK/insights/kpis/', 'videopath.apps.admin.views.kpis.view'),
   url(r'^YT58Pc3u6ZlK/insights/users/(?P<username>.+)/', 'videopath.apps.admin.views.users.userview'),
   url(r'^YT58Pc3u6ZlK/insights/users/', 'videopath.apps.admin.views.users.listview'),
   url(r'^YT58Pc3u6ZlK/insights/userstats/', 'videopath.apps.admin.views.userstats.view'),
   url(r'^YT58Pc3u6ZlK/insights/videos/', 'videopath.apps.admin.views.videos.view'),
   url(r'^YT58Pc3u6ZlK/insights/billing/', 'videopath.apps.admin.views.billing.view'),
   url(r'^YT58Pc3u6ZlK/insights/', 'videopath.apps.admin.views.base.view'),
   url(r'^YT58Pc3u6ZlK/health/', 'videopath.apps.admin.views.health_check.view'),
   )
