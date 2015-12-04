from django.conf.urls import url, patterns, include

from rest_framework import routers

from videopath.apps.users.views import UserViewSet, TeamViewSet, TeamMemberViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet, base_name="user")

router.register(r'team', TeamViewSet, base_name="team")
router.register(r'team/(?P<tid>[0-9]+)/member', TeamMemberViewSet, base_name="team_member")

urlpatterns = patterns('',

	# get token, delete token (aka logout)
    url(r'^api-token/', 'videopath.apps.users.views.api_token'),

    # reset password
    url(r'^user/me/password-reset', 'videopath.apps.users.views.password_reset'),

    url(r'', include(router.urls)),

)
