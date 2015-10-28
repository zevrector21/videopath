from videopath.apps.videos.tests.endpoints.endpoints_base import EndpointsBaseTestCase

INTEGRATION_URL = '/v1/integration/'

# Uses the standard django frame testing client
class TestCase(EndpointsBaseTestCase):

    def test_list_integrations(self):
        self.setup_users_and_clients()

        # should show mailchimp integration
        response = self.client_user1.get_json(INTEGRATION_URL)
        print response



