from django.contrib.auth.models import User as _User

#
# Proxy user model for Sales list
#
class User(_User):
    class Meta:
        proxy = True
