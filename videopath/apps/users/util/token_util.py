from datetime import datetime, timedelta, date

from django.core.cache import cache

from rest_framework import exceptions

from videopath.apps.users.models import AuthenticationToken, UserActivity, UserActivityDay

def authenticate_token(key):
	
	# try to load user and token from key	
	user, token = _load_user_and_token(key)

	# last seen
	_track_activity(user)

	# last seen per day
	_track_activity_daily(user)

	return user, token

#
# Try to validate access token
#
def _load_user_and_token(key):
	# try to find user in cache
	user = cache.get(key + "-user")
	token = cache.get(key + "-token")

	# try to find token
	if not user or not token:
	    try:
	        token = AuthenticationToken.objects.get(key=key)
	        user = token.user
	        cache.set(key + "-user", user, 60 * 5)  # save for 5 minutes
	        cache.set(key + "-token", token, 60 * 5)  # save for 5 minutes
	    except AuthenticationToken.DoesNotExist:
	        raise exceptions.AuthenticationFailed('Invalid token')

	#
	if not user.is_active:
	    raise exceptions.AuthenticationFailed('User inactive or deleted')

	# update last used timestamp if it's older than 10 minutes
	thresh = datetime.now() - timedelta(minutes=10)
	if token:
	    if token.last_used < thresh:
	        token.last_used = datetime.now()
	        token.save()

	return user, token


#
# keep a log of the last activity time
#
def _track_activity(user):
	thresh = datetime.now() - timedelta(minutes=10)
	cachekey = user.username + "-activity"
	activity = cache.get(cachekey)
	if not activity:
	    try:
	        activity = user.activity
	    except UserActivity.DoesNotExist:
	        activity, created = UserActivity.objects.get_or_create(user=user)
	        activity.last_seen=datetime.now()
	        activity.save()
	    cache.set(cachekey, activity)

	if activity and activity.last_seen < thresh:
	    activity.last_seen = datetime.now()
	    activity.save()
	    cache.set(cachekey, activity)

#
# Keep a log of when the users were here
#
def _track_activity_daily(user):
	today = date.today()
        cachekey = user.username + "-day-" + str(today)
        activity = cache.get(cachekey)
        if not activity:
            activity, created = UserActivityDay.objects.get_or_create(user=user, day=today)
            cache.set(cachekey, activity)