
from videopath.apps.common.test_utils import BaseTestCase
from videopath.apps.videos.models import Video, Marker, MarkerContent
from videopath.apps.files.models import VideoFile, ImageFile


# Uses the standard django frame testing client
class ImageTests(BaseTestCase):

    def setUp(self):
        self.setup_users()

    # not working right now
    def test_signals(self):

        # create video file
        v = Video.objects.create(user=self.user1)
        vf = VideoFile.objects.create(video=v)


    def test_image_file_delete(self):

        # create one video with an image file attached
        v = Video.objects.create(user=self.user1)
        m = Marker.objects.create(video_revision=v.draft)
        c = MarkerContent.objects.create(marker=m)
        imf = ImageFile.objects.create()
        imf.markercontent.add(c)
        imf.save()
        self.assertEqual(ImageFile.objects.count(), 1)

        # create new draft
        v.publish()
        v.create_new_draft()
        self.assertEqual(ImageFile.objects.count(), 1)
        self.assertEqual(v.revisions.count(), 2)
        self.assertEqual(imf.markercontent.count(), 2)

        # deleting revision should not affect image file
        self.assertEqual(Marker.objects.count(), 2)
        self.assertEqual(v.draft.markers.count(), 1)
        v.draft.delete()
        self.assertEqual(Marker.objects.count(), 1)
        self.assertEqual(MarkerContent.objects.count(), 1)
        self.assertEqual(ImageFile.objects.count(), 1)
        self.assertEqual(imf.markercontent.count(), 1)

        # deleting the draft should delete the image file though
        v.current_revision.delete()
        self.assertEqual(v.revisions.count(), 0)
        self.assertEqual(MarkerContent.objects.count(), 0)
        self.assertEqual(Marker.objects.count(), 0)

        # now nothing is around any more...
        self.assertEqual(imf.markercontent.count(), 0)
        self.assertEqual(ImageFile.objects.count(), 0)
