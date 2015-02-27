
from videopath.apps.common.test_utils import BaseTestCase
from videopath.apps.videos.models import Video
from videopath.apps.files.models import VideoFile

# Uses the standard django frame testing client
class TestCase(BaseTestCase):

    def setup(self):
        self.create_user()

    def test_creation(self):
    	video = Video.objects.create(user=self.user)
    	f = VideoFile.objects.create(video=video)
        self.assertIsNotNone(f)