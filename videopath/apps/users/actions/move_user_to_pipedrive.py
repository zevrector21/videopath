import requests

from django.conf import settings

from videopath.apps.users.models import UserSalesInfo, UserCampaignData

PIPEDRIVE_API_KEY = settings.PIPEDRIVE_API_KEY

PIPEDRIVE_BASE_URL = 'https://api.pipedrive.com/v1'

PIPEDRIVE_PERSON_URL = PIPEDRIVE_BASE_URL + '/persons'
PIPEDRIVE_FIND_PERSON_URL = PIPEDRIVE_PERSON_URL + '/find'
PIPEDRIVE_DEAL_URL = PIPEDRIVE_BASE_URL + '/deals'
PIPEDRIVE_ORG_URL = PIPEDRIVE_BASE_URL + '/organizations'
PIPEDRIVE_NOTE_URL = PIPEDRIVE_BASE_URL + '/notes'

DEFAULT_STAGE_ID = 12
SOURCE_FIELD_ID = 'c74438c341d64dadce88fec9796605a73daa2057'
USER_ID = 823305 # anthony


def run(user, only_check_and_link = False):

	person_id = _get_person_by_email(user.email)
	if person_id >= 0:
		return _link_user_to_pipedrive_person(user,person_id)
	if only_check_and_link:
		return None
	person_id = _create_person_in_pipedrive(user)
	return _link_user_to_pipedrive_person(user,person_id)


def _link_user_to_pipedrive_person(user, person_id):
	info, created = UserSalesInfo.objects.get_or_create(user=user)
	info.pipedrive_person_id = person_id
	info.save()
	return info

def _get_person_by_email(email):
	params = {
		'term': email,
		'search_by_email': 1
	}
	result = _pipedrive_get(PIPEDRIVE_FIND_PERSON_URL, params)['data']
	if result and len(result):
		return result[0].get('id')
	return None 

def _create_person_in_pipedrive(user):

	email = user.email

	# create person
	data = {
		'email': email,
		'name': email,
		'visible_to': 3,
		'owner_id': USER_ID
	}
	person_id = _pipedrive_post(PIPEDRIVE_PERSON_URL, data=data)['data']['id']

	# create org
	data = {
		'name': "Inbound " + email,
		SOURCE_FIELD_ID: 78,
		'visible_to': 3,
		'owner_id': USER_ID
	}
	#print _pipedrive_post(PIPEDRIVE_ORG_URL, data=data)['data']['id']
	org_id = _pipedrive_post(PIPEDRIVE_ORG_URL, data=data)['data']['id']

	# also create a deal
	data = {
		'title': "Inbound " + email,
		'person_id': person_id,
		'org_id': org_id,
		'stage_id': DEFAULT_STAGE_ID,
		'value': 2000,
		'currency': "EUR",
		'visible_to': 3,
		'user_id': USER_ID
	}
	deal_id = _pipedrive_post(PIPEDRIVE_DEAL_URL, data=data)['data']['id']

	# add notes to user and deal
	try:	
		content  = 'Country: ' + user.campaign_data.country + '<br />'
		content += 'Campaign: ' + user.campaign_data.name + '<br />'
		content += 'Referrer: ' + user.campaign_data.referrer + '<br />'
		data = {
			'content': content,
			'deal_id': deal_id,
			'person_id': person_id,
			'org_id': org_id
		}
		_pipedrive_post(PIPEDRIVE_NOTE_URL, data=data)
	except UserCampaignData.DoesNotExist:
		pass

	return person_id


#
# Pipedrive helpers
#
def _pipedrive_get(url, params = {}):
	params['api_token'] = PIPEDRIVE_API_KEY
	return requests.get(url, params=params).json()


def _pipedrive_post(url, params = {}, data = {}):
	params['api_token'] = PIPEDRIVE_API_KEY
	result = requests.post(url, params=params, data=data)
	return result.json()