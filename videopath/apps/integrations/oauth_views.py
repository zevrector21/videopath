from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from services import config

from .models import Integration

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
	credentials = service_config['module'].handle_oauth2_request(request, user)
	if credentials:
		try:
			integration = Integration.objects.get(user=user, service=service)
			integration.delete()
		except Integration.DoesNotExist:
			pass
		Integration.objects.create(user=user, service=service, credentials=credentials)

		return HttpResponseRedirect(SUCCESS_URL)

	return HttpResponseRedirect(FAIL_URL)

