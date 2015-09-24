from videopath.apps.common.test_utils import BaseTestCase

from videopath.apps.videos.models import Video

IMPORT_URL = '/v1/video/{0}/import_source/'

# Uses the standard django frame testing client
class TestCase(BaseTestCase):

    def test_youtube_import(self):

        # create user and video
        self.setup_users_and_clients()
        v=Video.objects.create(user=self.user)

        response = self.client_user1.post(IMPORT_URL.format(v.pk), {'url':'https://www.youtube.com/watch?v=PPN3KTtrnZM'})
        self.assertEqual(response.status_code, 200)

        v = Video.objects.get(pk=v.id)
        self.assertEqual(v.draft.source.service, "youtube")

    def test_vimeo_import(self):
        # create user and video
        self.setup_users_and_clients()
        v=Video.objects.create(user=self.user)

        response = self.client_user1.post(IMPORT_URL.format(v.pk), {'url':'https://vimeo.com/36579366'})
        self.assertEqual(response.status_code, 200)

        v = Video.objects.get(pk=v.id)
        self.assertEqual(v.draft.source.service, "vimeo")

    def test_wistia_import(self):
        # create user and video
        self.setup_users_and_clients()
        v=Video.objects.create(user=self.user)

        response = self.client_user1.post(IMPORT_URL.format(v.pk), {'url':'http://home.wistia.com/medias/1gaiqzxu03'})
        self.assertEqual(response.status_code, 200)

        v = Video.objects.get(pk=v.id)
        self.assertEqual(v.draft.source.service, "wistia")

    def test_brightcove_import(self):
        # create user and video
        self.setup_users_and_clients()
        v=Video.objects.create(user=self.user)

        #response = self.client_user1.post(IMPORT_URL.format(v.pk), {'url':'http://players.brightcove.net/4328472451001/default_default/index.html?videoId=4332059708001'})
        #self.assertEqual(response.status_code, 200)
        v = Video.objects.get(pk=v.id)

        # disable brightcove import for now

    def test_custom_import(self):
        self.setup_users_and_clients()
        v=Video.objects.create(user=self.user)
        data = {
            "mp4":"http://videos.videopath.com/m35T1YU0KHQ8ZEr28fKgM4sS0zfEOQW3.mp4",
            "webm": "http://videos.videopath.com/m35T1YU0KHQ8ZEr28fKgM4sS0zfEOQW3.webm",
            "width":"320",
            "height":"240",
            "duration":"200"
          }
        response = self.client_user1.post(IMPORT_URL.format(v.pk), data)
        self.assertEqual(response.status_code, 200)

        v = Video.objects.get(pk=v.id)
        self.assertEqual(v.draft.source.service, "custom")
        
