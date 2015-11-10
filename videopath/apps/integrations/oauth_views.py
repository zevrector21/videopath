
from django.http import HttpResponseRedirect

from services import config

from django.conf import settings

from .util import oauth2_util


# redirect urls
FAIL_URL = settings.APP_URL + '/#integrations?result=failure'
SUCCESS_URL = settings.APP_URL + '/#integrations?result=success'


#
# Receive oauth requests
#
def oauth_receive(request, service):

	# find service definition
	try:
		service_config = config[service]
	except:
		return HttpResponseRedirect(FAIL_URL)	

	if oauth2_util.handle_redirect(request, service_config):
		return HttpResponseRedirect(SUCCESS_URL)
	return HttpResponseRedirect(FAIL_URL)

