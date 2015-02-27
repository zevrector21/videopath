
from videopath.apps.videos.models import Video
from videopath.apps.common.test_utils import BaseTestCase

from videopath.apps.videos.util import video_export_util

# Uses the standard django frame testing client
class TestCase(BaseTestCase):

    def setup(self):
        self.create_user()

    def test_export_video(self):
        
        # video should be creatable 
        video = Video.objects.create(user=self.user)
       	video_export_util.export_video(video)

