
from videopath.apps.videos.models import Video, MarkerContent, Marker
from videopath.apps.common.test_utils import BaseTestCase

# Uses the standard django frame testing client
class TestCase(BaseTestCase):

    def setup(self):
        self.create_user()

    def test_creation(self):
        video = Video.objects.create(user=self.user)
        self.assertIsNotNone(video.draft)

    def test_duplication(self):
    	video = Video.objects.create(user=self.user)

    	markers =[
    		Marker.objects.create(video_revision=video.draft),
    		Marker.objects.create(video_revision=video.draft),
    	]

    	MarkerContent.objects.create(marker=markers[0])
    	MarkerContent.objects.create(marker=markers[0])
    	MarkerContent.objects.create(marker=markers[0])
    	MarkerContent.objects.create(marker=markers[1])

    	video.draft.duplicate()

    	self.assertEqual(Marker.objects.count(), 4)
    	self.assertEqual(MarkerContent.objects.count(), 8)





