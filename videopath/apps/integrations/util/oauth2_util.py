import urllib, hashlib

from datetime import date

from ..models import Integration
from django.contrib.auth.models import User


def hash_user(user):
	return hashlib.sha224(str(user.pk) + user.email + str(date.today)).hexdigest()

def authorize_uri_for_user(service, user):

	if not 'oauth2' in service:
		return ''

	params = {
		'redirect_uri': service['oauth2']['redirect_url'],
		'client_id': service['oauth2']['client_id'],
		'response_type': 'code',
		'state': str(user.pk) + ' ' + hash_user(user)
	}

	if 'scope' in service['oauth2']:
		params['scope'] = service['oauth2'].get('scope')

	return service['oauth2']['authorize_url'] + '?' + urllib.urlencode(params)


def handle_redirect(request, service):

	state = request.GET.get('state','')
	code = request.GET.get('code','')

	print state + ' ' + code

	# try to load user
	try:
		uid = int(state.split(' ')[0])
		user = User.objects.get(pk=uid)
	except User.DoesNotExist:
		return False

	# try to handle oauth in service module
	credentials = service['module'].handle_redirect(service, user, code)
	if credentials:
		try:
			integration = Integration.objects.get(user=user, service=service)
			integration.delete()
		except Integration.DoesNotExist:
			pass
		Integration.objects.create(user=user, service=service['id'], credentials=credentials)

		return True

	return False