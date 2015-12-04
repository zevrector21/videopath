from videopath.apps.videos.tests.endpoints.endpoints_base import EndpointsBaseTestCase

TEAM_URL = '/v1/team/'
TEAMMEMBER_URL = '/v1/team/{1}/'

# Uses the standard django frame testing client
class TestCase(EndpointsBaseTestCase):

	def test_anonymous_access(self):
		self.setup_users_and_clients()
		response = self.client.get_json(TEAM_URL)
		self.assertEqual(response.status_code, 403)

	def test_ensure_default_team(self):
		self.setup_users_and_clients()
		response = self.client_user1.get_json(TEAM_URL)
		self.assertEqual(response.data.get('count'), 1)


