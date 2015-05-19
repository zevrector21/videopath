from django.conf.urls import url, patterns, include

from rest_framework import routers

from videopath.apps.users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet, base_name="user")

urlpatterns = patterns('',

	# get token, delete token (aka logout)
    url(r'^api-token/', 'videopath.apps.users.views.api_token'),

    # reset password
    url(r'^user/me/password-reset', 'videopath.apps.users.views.password_reset'),

    url(r'', include(router.urls)),

    url(r'^user/ip-check', 'videopath.apps.users.views.ip_check'),

)
