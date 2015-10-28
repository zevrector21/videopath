from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

import requests

# redirect urls
FAIL_URL = 'http://localhost/app/dist/#integrations?result=failure'
SUCCESS_URL = 'http://localhost/app/dist/#integrations?result=success'

# mailchimp urls
MAILCHIMP_TOKEN_URL = 'https://login.mailchimp.com/oauth2/token'

#
# Receive oauth requests
#
def oauth_receive(request, service, uid):
	# try to load user
	try:
		user = User.objects.get(pk=uid)
	except User.DoesNotExist:
		return HttpResponseRedirect(FAIL_URL)

	if service == 'mailchimp':
		return oauth_mailchimp(request, user)

	return HttpResponseRedirect(FAIL_URL)

#
# process mailchimp
#
def oauth_mailchimp(request, user):
	
	code = request.GET.get('code', '')
	print code

	headers = {'content-type': 'application/x-www-form-urlencoded'}
	data = {
		'grant_type': 'authorization_code',
		'client_id': '351116972183',
		'client_secret': 'c8318f8c5efa30b314ca22fbcdd6a889',
		'code': code,
		'redirect_uri': 'http://127.0.0.1:5000/oauth/receive/mailchimp/1/'
	}

	response = requests.post(MAILCHIMP_TOKEN_URL, headers = headers, data=data)
	token = response.json().get('access_token', '')

	if not token:
		return HttpResponseRedirect(FAIL_URL)
	
	return HttpResponseRedirect(SUCCESS_URL)

