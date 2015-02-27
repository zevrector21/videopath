from django.test import TestCase

from videopath.apps.files.models import VideoFile
from videopath.apps.files.thumbnail_manager import ThumbnailManager
from videopath.apps.videos.models import *
from videopath.apps.common.test_utils import *

class ThumbnailsTest(TestCase):

    def setUp(self):
        self.user1 = create_simple_user()
        self.video = Video.objects.create(user=self.user1)
        self.videoFile = VideoFile.objects.create(
            video_id=self.video.id, video_duration=202, status=VideoFile.TRANSCODING_COMPLETE)
        self.video.save()

        self.manager = ThumbnailManager()

    # not working right now
    def test_manager(self):
        thumbs = self.manager.available_thumbs_for_video(self.video)
        default = self.manager.current_thumbnail_index_for_video(self.video)

        # default thumb should be two
        self.assertEqual(default, 2)

        # should be 4 thumbs available
        self.assertEqual(len(thumbs), 4)

        self.manager.set_thumbnail_index_for_video(self.video, 3)
        self.assertEqual(
            self.manager.current_thumbnail_index_for_video(self.video), 3)
