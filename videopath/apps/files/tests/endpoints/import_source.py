from videopath.apps.common.test_utils import BaseTestCase

from videopath.apps.videos.models import Video
from videopath.apps.files.models import VideoSource

IMPORT_URL = '/v1/video/{0}/import_source/'

# Uses the standard django frame testing client
class TestCase(BaseTestCase):

    def test_youtube_import(self):

        # create user and video
        self.setup_users_and_clients()
        v=Video.objects.create(user=self.user)

        response = self.client_user1.post(IMPORT_URL.format(v.pk), {'url':'https://www.youtube.com/watch?v=PPN3KTtrnZM'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(VideoSource.objects.first().service, "youtube")

    def test_vimeo_import(self):
        # create user and video
        self.setup_users_and_clients()
        v=Video.objects.create(user=self.user)

        response = self.client_user1.post(IMPORT_URL.format(v.pk), {'url':'https://vimeo.com/36579366'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(VideoSource.objects.first().service, "vimeo")

    def test_wistia_import(self):
        # create user and video
        self.setup_users_and_clients()
        v=Video.objects.create(user=self.user)

        response = self.client_user1.post(IMPORT_URL.format(v.pk), {'url':'http://home.wistia.com/medias/1gaiqzxu03'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(VideoSource.objects.first().service, "wistia")

