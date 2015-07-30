
from videopath.apps.videos.models import Video
from videopath.apps.common.test_utils import BaseTestCase

from videopath.apps.files.models import VideoSource, VideoFile

# Uses the standard django frame testing client
class TestCase(BaseTestCase):

    def setup(self):
        self.create_user()

    def test_creation(self):
        
        # video should be creatable 
        video = Video.objects.create(user=self.user)
       	self.assertIsNotNone(video)

       	# video should have draft revision
       	self.assertIsNotNone(video.draft)

    def test_publish_unpublish(self):
      	video = Video.objects.create(user=self.user)
      	video.publish()
      	video.unpublish()