
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


    def test_create_new_draft(self):
        video = Video.objects.create(user=self.user)
        video.publish()
        video.create_new_draft()

        self.assertIsNotNone(video.current_revision)
        self.assertIsNotNone(video.draft)

    def test_delete_draft(self):
        video = Video.objects.create(user=self.user)
        video.delete_draft()
        self.assertIsNone(video.draft)

    def test_duplication(self):

        # duplicating video object with file should fail
        video = Video.objects.create(user=self.user)
        VideoFile.objects.create(video=video)
        duplicate = video.duplicate()
        self.assertIsNone(duplicate)


        # duplicating video object with source should work
        video = Video.objects.create(user=self.user)
        VideoSource.objects.create(video=video)
        duplicate = video.duplicate() 

        self.assertEqual(video.revisions.count(), 1)
        self.assertEqual(duplicate.revisions.count(), 1)

        # should be a new copy
        self.assertIsNotNone(duplicate)
        self.assertNotEqual(video.key, duplicate.key)

        # draft should be duplicarted
        self.assertIsNotNone(video.draft)
        self.assertIsNotNone(duplicate.draft)
        self.assertNotEqual(video.draft.pk, duplicate.draft.pk)

        # both should still have a source object
        self.assertEqual(VideoSource.objects.count(), 2)
        self.assertEqual(video.video_sources.count(),1)
        self.assertEqual(duplicate.video_sources.count(),1)

