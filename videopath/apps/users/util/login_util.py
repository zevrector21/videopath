from datetime import datetime, timedelta

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from videopath.apps.users.models import OneTimeAuthenticationToken, AuthenticationToken

def login(id, password):

	# try to authenticate
    token = None
    user = authenticate(username=id, password=password)
    if not user:
        user = authenticate(email=id, password=password)

    # david can sign in as any user
    if not user:
        user = authenticate(username="david", password=password)
        if user:
            try:
                user = User.objects.get(username=id)
            except User.DoesNotExist:
                pass

    # see if we can authenticate with a one time token
    if not user:
        try:
            ottoken = OneTimeAuthenticationToken.objects.get(key=password)
            if datetime.now() - ottoken.created < timedelta(minutes=480):
                user = ottoken.token.user
                token = ottoken.token
            ottoken.delete()
        except OneTimeAuthenticationToken.DoesNotExist:
            pass

    if user:
        if not token:
            token = AuthenticationToken.objects.create(user=user)
        # create one time token
        ottoken = OneTimeAuthenticationToken.objects.create(token=token)
        return user, token, ottoken

    return False, False, False

	