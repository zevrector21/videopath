
from videopath.apps.videos.models import Video, Marker, MarkerContent
from videopath.apps.common.test_utils import BaseTestCase

# Uses the standard django frame testing client
class UploadEndpoints(BaseTestCase):

    def setUp(self):
        self.setup_users_and_clients()
        self.video = Video.objects.create(user=self.user1)
        self.marker = Marker.objects.create(video_revision=self.video.draft)
        self.content = MarkerContent.objects.create(marker=self.marker)

    def test_files_endpoints(self):

        pass
        # legacy endpoint
        # response = self.client_user1.get(
        #     '/endpoints/files/v1/image/upload/requestticket/' + str(self.content.id) + "/")
        # self.assertEqual(response.status_code, 200)

        # # new marker content image endpoint
        # response = self.client_user1.get(
        #     '/endpoints/files/v1/image/upload/requestticket/marker_content/' + str(self.content.id) + "/")
        # self.assertEqual(response.status_code, 200)

        # response = self.client_user1.get(
        #     '/endpoints/files/v1/image/upload/requestticket/custom_thumbnail/' + str(self.video.draft.id) + "/")
        # self.assertEqual(response.status_code, 200)

        # response = self.client_user1.get(
        #     '/endpoints/files/v1/image/upload/requestticket/custom_logo/' + str(self.video.draft.id) + "/")
        # self.assertEqual(response.status_code, 200)
