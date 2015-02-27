
from videopath.apps.common.test_utils import BaseTestCase
from videopath.apps.videos.models import Video
from videopath.apps.files.models import VideoSource

# Uses the standard django frame testing client
class TestCase(BaseTestCase):

    def setup(self):
        self.create_user()

    def test_creation(self):
    	video = Video.objects.create(user=self.user)
    	s = VideoSource.objects.create(video=video)
        self.assertIsNotNone(s)