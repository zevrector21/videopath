import requests
import re

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):

		print "Importing Brightcove..."

		# settings
		re_url = 'brightcove.net\/([0-9]*)\/([0-9a-z\-]*)_([0-9a-z\-]*)\/index.html\?videoId=([0-9]*)'
		re_pk = 'policyKey:"([A-Za-z0-9-_]*)"'
		api_url = 'https://edge.api.brightcove.com/playback/v1/accounts/{0}/videos/{1}'

		# inpurt
		url = "http://players.brightcove.net/4333019801001/8c899937-a881-49a2-a557-72b4764d7d2d_default/index.html?videoId=4334023184001"

		#fish out details
		m = re.search(re_url, url)
		video_id = m.group(4)
		player_id = m.group(2)
		account_id = m.group(1)

		print "-> Found Video ID: " + video_id
		print "-> Found Player ID: " + player_id
		print "-> Found Account ID: " + account_id

		# fish out policy key
		response = requests.get(url)
		m = re.search(re_pk, response.text)
		policy_key = m.group(1)
		print "-> Found policy key: " + policy_key

		# fish out video defintions
		url = api_url.format(account_id, video_id)
		headers = {"BCOV-Policy":policy_key}
		response = requests.get(url, headers=headers)
		json_data = response.json()
		source = json_data["sources"][0]

		thumbnail = json_data["thumbnail"]
		print "-> Found Video Thumbnail: " + thumbnail

		duration = json_data["duration"]
		print "-> Found Video Duration: " + str(duration)

		width = source["width"]
		height = source["height"]
		print "-> Found dimensions: " + str(width) + "x" + str(height)



