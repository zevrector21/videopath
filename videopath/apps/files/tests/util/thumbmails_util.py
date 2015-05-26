from django.test import TestCase

from videopath.apps.files.models import VideoFile
from videopath.apps.files.util import thumbnails_util
from videopath.apps.videos.models import Video
from videopath.apps.common.test_utils import create_simple_user

class ThumbnailsTest(TestCase):

    def setUp(self):
        self.user1 = create_simple_user()
        self.video = Video.objects.create(user=self.user1)
        self.videoFile = VideoFile.objects.create(
            video_id=self.video.id, video_duration=202, status=VideoFile.TRANSCODING_COMPLETE)
        self.video.save()


    # not working right now
    def test_manager(self):
        thumbs = thumbnails_util.available_thumbs_for_video(self.video)
        default = thumbnails_util.current_thumbnail_index_for_video(self.video)

        # default thumb should be two
        self.assertEqual(default, 2)

        # should be 4 thumbs available
        self.assertEqual(len(thumbs), 4)

        thumbnails_util.set_thumbnail_index_for_video(self.video, 3)
        self.assertEqual(
            thumbnails_util.current_thumbnail_index_for_video(self.video), 3)
