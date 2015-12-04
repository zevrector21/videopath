from videopath.apps.videos.tests.endpoints.endpoints_base import EndpointsBaseTestCase

from videopath.apps.users.models import Team, TeamMember

TEAM_URL = '/v1/team/'
TEAMMEMBER_NESTED_URL = '/v1/team/{0}/team-member/'
TEAMMEMBER_URL = '/v1/team-member/'

# Uses the standard django frame testing client
class TestCase(EndpointsBaseTestCase):

	def test_anonymous_access(self):
		self.setup_users_and_clients()

		response = self.client.get_json(TEAMMEMBER_URL)
		self.assertEqual(response.status_code, 403)

		response = self.client.get_json(TEAMMEMBER_NESTED_URL.format(self.user1.default_team.pk))
		self.assertEqual(response.status_code, 403)

	def test_adding_members(self):

		# adding members
		self.setup_users_and_clients()

		response = self.client_user1.post_json(TEAM_URL, {})
		self.assertEqual(response.status_code, 201)
		team_id = response.data.get('id')

		# user 1, the owner, can add members
		response = self.client_user1.post_json(TEAMMEMBER_NESTED_URL.format(team_id), {'email': self.user2.email, 'team': team_id})
		self.assertEqual(response.status_code, 201)

		# but not from unknown email addresses
		response = self.client_user1.post_json(TEAMMEMBER_NESTED_URL.format(team_id), {'email': 'blah@gmx.net', 'team': team_id})
		self.assertEqual(response.status_code, 404)


		# deleting members

