from django.test import TestCase

from videopath.apps.common.test_utils import create_simple_user
from videopath.apps.videos.models import Video
from videopath.apps.files import video_source_importers

# Uses the standard django frame testing client
class VimeoTests(TestCase):

    def setUp(self):
        self.user1 = create_simple_user()
        self.video = Video.objects.create(user=self.user1)

    # not working right now
    def test_vimeo(self):

        # borked yt ID should produce no result
        result, message = video_source_importers.import_url(
            self.video, "https://www.vimeo.com/38849923023")
        self.assertFalse(result)

        result, message = video_source_importers.import_url(
            self.video, "https://vimeo.com/6235286")
        self.assertNotEqual(result, False)
