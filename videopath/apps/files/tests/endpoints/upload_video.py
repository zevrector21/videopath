from videopath.apps.common.test_utils import BaseTestCase
from videopath.apps.videos.models import Video
from videopath.apps.files.models import VideoFile

REQUEST_URL = '/v1/video/upload/requestticket/{0}/'
COMPLETE_URL = '/v1/video/upload/complete/{0}/'

# Uses the standard django frame testing client
class TestCase(BaseTestCase):

    def test_upload_video(self):

        self.setup_users_and_clients()
        v=Video.objects.create(user=self.user)

        # test creation of ticket
        response = self.client_user1.get(REQUEST_URL.format(v.pk))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(VideoFile.objects.count(), 1)

        ticket_id = response.data["ticket_id"]

        # test complete notification
        response = self.client_user1.get(COMPLETE_URL.format(ticket_id))
        self.assertEqual(response.status_code, 200)


