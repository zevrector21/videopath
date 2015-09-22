from django.test import TestCase

from videopath.apps.files.models import VideoFile, VideoSource
from videopath.apps.files.util import source_util
from videopath.apps.videos.models import Video
from videopath.apps.common.test_utils import create_simple_user

class SourceTest(TestCase):

    def setUp(self):
        self.user1 = create_simple_user()
        self.video = Video.objects.create(user=self.user1)
        self.video.save()


    def test_jpg_sequence_support(self):
        self.video.draft.iphone_images = 200
        self.video.draft.save()
        source = source_util.source_for_revision(self.video.draft)
        self.assertEqual(source['jpg_sequence_length'], 200)

    def test_old_source_object(self):
        VideoSource.objects.create(
            video=self.video,
            service='youtube',
            service_identifier='12345')

        source = source_util.source_for_revision(self.video.draft)
        self.assertEqual(source['service'], 'youtube')
        self.assertEqual(source['service_identifier'], '12345')

    def test_old_file_object(self):
        VideoFile.objects.create(
            video=self.video,
            video_width=1024,
            video_height= 768)

        source = source_util.source_for_revision(self.video.draft)
        self.assertEqual(source['service'], 'videopath')
        self.assertTrue(source['aspect'] > 1.3 )
        self.assertIsNotNone(source['file_mp4'])
        self.assertIsNotNone(source['file_webm'])
