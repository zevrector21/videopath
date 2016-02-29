from django.contrib.auth.models import User as _User
from videopath.apps.videos.models import Video as _Video

#
# Proxy user model for Sales list
#
class User(_User):
    class Meta:
        proxy = True

#
# Proxy model for videos
#
class Video(_Video):
	class Meta:
		proxy = True