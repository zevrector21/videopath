#
# Login a user with email and passoword or token
#

from datetime import datetime, timedelta

from django.contrib.auth import authenticate
from videopath.apps.users.models import User

from videopath.apps.users.models import OneTimeAuthenticationToken, AuthenticationToken

def run(id, password):

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
                user = User.objects.get(username__iexact=id)
            except User.DoesNotExist:
                try:
                    user = User.objects.get(email__iexact=id)
                except User.DoesNotExist:
                    user = None


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

	