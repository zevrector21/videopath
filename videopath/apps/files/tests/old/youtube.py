from django.test import TestCase

from videopath.apps.videos.models import Video
from videopath.apps.common.test_utils import create_simple_user
from videopath.apps.files import video_source_importers

# Uses the standard django frame testing client
class YoutubeTests(TestCase):

    def setUp(self):
        self.user1 = create_simple_user()
        self.video = Video.objects.create(user=self.user1)

    def test_random_import(self):
        result, message = video_source_importers.import_url(
            self.video, "http://google.com/something")
        self.assertFalse(result)

    # not working right now
    def test_youtube(self):

        # borked yt ID should produce no result
        result, message = video_source_importers.import_url(
            self.video, "https://www.youtube.com/v/something")
        self.assertFalse(result)

        result, message = video_source_importers.import_url(
            self.video, "https://www.youtube.com/watch?v=ilWWl4UdN74")
        self.assertNotEqual(result, False)
