from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from services import config

from django.conf import settings

# redirect urls
FAIL_URL = settings.APP_URL + '/#integrations?result=failure'
SUCCESS_URL = settings.APP_URL + '/#integrations?result=success'


#
# Receive oauth requests
#
def oauth_receive(request, service, uid):

	# try to load user
	try:
		user = User.objects.get(pk=uid)
	except User.DoesNotExist:
		return HttpResponseRedirect(FAIL_URL)

	# find service definition
	try:
		service_config = config[service]
	except:
		return HttpResponseRedirect(FAIL_URL)	

	# try to handle oauth in service module
	if service_config['module'].handle_oauth2_request(request, user):
		return HttpResponseRedirect(SUCCESS_URL)

	return HttpResponseRedirect(FAIL_URL)

