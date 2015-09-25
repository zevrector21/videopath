from videopath.apps.videos.tests.endpoints.endpoints_base import EndpointsBaseTestCase

from videopath.apps.videos.models import Video

BASE_URL = '/v1/'
VIDEO_URL = BASE_URL + 'video/'

# 
PUBLISHED_REVISION_URL = BASE_URL + 'video/{0}/revision/published/'
DRAFT_URL = BASE_URL + 'video/{0}/revision/draft/'

PUBLISHED_REVISION_URL_EXPANDED = BASE_URL + 'video/{0}/revision/published/?expanded=1'
DRAFT_URL_EXPANDED = BASE_URL + 'video/{0}/revision/draft/?expanded=1'

# publish and unpublish
PUBLIC_URL = BASE_URL + 'video/{0}/public/'

# send share
SEND_SHARE_MAIL_URL = BASE_URL + 'video/{0}/share-email/'

# Uses the standard django frame testing client
class TestCase(EndpointsBaseTestCase):


    def test_get_access(self):
        self.setup_users_clients_and_videos()

        # no access without login
        response = self.client.get(VIDEO_URL)
        self.assertEqual(response.status_code, 403)

        # access with login
        response = self.client_user1.get(VIDEO_URL)
        self.assertEqual(response.status_code, 200)

    def test_creation(self):
        
        self.setup_users_and_clients()

        # regular video
        response = self.client_user1.post_json(VIDEO_URL, {})
        self.assertEqual(response.status_code, 201)


    def test_import_demo(self):
        self.setup_users_clients_and_videos()

        # video with demo
        response = self.client_user1.post_json(VIDEO_URL, {"demo_project":"1"})
        self.assertEqual(response.status_code, 201)
        # assert that this video now has a video source (the youtube demo)
        self.assertIsNotNone(Video.objects.get(pk=response.data["id"]).draft.source) 

    def test_publish(self):
        self.setup_users_clients_and_videos()
        vid = self.video.pk

        # access draft and revision
        response = self.client_user1.get(DRAFT_URL.format(vid))
        self.assertEqual(response.status_code, 200)
        response = self.client_user1.get(PUBLISHED_REVISION_URL.format(vid))
        self.assertEqual(response.status_code, 404)

        # try to publish
        response = self.client_user1.put(PUBLIC_URL.format(vid))
        self.assertEqual(response.status_code, 200)

        # access draft and revision
        response = self.client_user1.get(DRAFT_URL_EXPANDED.format(vid))
        self.assertEqual(response.status_code, 200)
        response = self.client_user1.get(PUBLISHED_REVISION_URL_EXPANDED.format(vid))
        self.assertEqual(response.status_code, 200)

        # unpublish
        response = self.client_user1.delete(PUBLIC_URL.format(vid))
        self.assertEqual(response.status_code, 200)

    def test_send_share_mail(self):
        self.setup_users_clients_and_videos()
        vid = self.video.pk

         # try to publish
        response = self.client_user1.put(PUBLIC_URL.format(vid))
        self.assertEqual(response.status_code, 200)

        # try to send share mail
        response = self.client_user1.post_json(SEND_SHARE_MAIL_URL.format(vid), {"recipients": "null@videopath.com"})
        self.assertEqual(response.status_code, 200)

        

        

        

        







