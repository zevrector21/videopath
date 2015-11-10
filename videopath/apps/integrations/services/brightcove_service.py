
import requests
from requests.auth import HTTPBasicAuth

ACCESS_TOKEN_URL = 'https://oauth.brightcove.com/v3/access_token'



def get_token(client_id, client_secret):
	headers = {
		'content-type': 'application/x-www-form-urlencoded'
	}
	response = requests.post(ACCESS_TOKEN_URL, 
		auth=HTTPBasicAuth(client_id, client_secret), 
		headers=headers,
		data={'grant_type':'client_credentials'})

	try:
		return response.json().get('access_token')
	except:
		return None

def handle_credential_request(credentials): 
	
	client_id = credentials.get('client_id')
	client_secret = credentials.get('client_secret')

	if get_token(client_id, client_secret):
		return credentials
	else:
		return None

	