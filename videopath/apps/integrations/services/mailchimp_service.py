import requests, urllib, mailchimp
from django.conf import settings


MAILCHIMP_TOKEN_URL = 'https://login.mailchimp.com/oauth2/token'
MAILCHIMP_METADATA_URL = 'https://login.mailchimp.com/oauth2/metadata'


def redirect_uri_for_user(user):
	return settings.API_ENDPOINT + '/oauth/receive/mailchimp/' + str(user.pk) + '/'

#
# Build oauth 2 starting point
#
def oauth2_endpoint_for_user(user):
	params = urllib.urlencode({
		'redirect_uri': redirect_uri_for_user(user),
		'client_id': settings.MAILCHIMP_CLIENT_ID,
		'response_type': 'code'
		})
	return 'https://login.mailchimp.com/oauth2/authorize?' + params

#
# handling incoming oauth request
#
def handle_oauth2_request(request, user):
	code = request.GET.get('code', '')

	# convert the code into an access token
	headers = {
		'content-type': 'application/x-www-form-urlencoded'
	}
	data = {
		'grant_type': 'authorization_code',
		'client_id': settings.MAILCHIMP_CLIENT_ID,
		'client_secret': settings.MAILCHIMP_CLIENT_SECRET,
		'code': code,
		'redirect_uri': redirect_uri_for_user(user)
	}

	response = requests.post(MAILCHIMP_TOKEN_URL, headers = headers, data=data)
	token = response.json().get('access_token', '')

	if not token:
		return False

	# complete the token to an api_key by getting the metadata for the datacenter
	headers = {
		'Authorization': 'OAuth ' + token,
		'Accept': 'application/json'
	}
	response = requests.get(MAILCHIMP_METADATA_URL, headers = headers)
	datacenter = response.json().get('dc', None)
	api_key = token + '-' + datacenter

	
	return {
		'api_key': api_key
	}