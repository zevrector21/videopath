
from videopath.apps.videos.models import Source
from videopath.apps.common.test_utils import BaseTestCase

from videopath.apps.videos.serializers import SourceSerializer

from django.conf import settings

# Uses the standard django frame testing client
class TestCase(BaseTestCase):

    def setup(self):
    	pass

    def test_videopath_source(self):
        source = Source.objects.create(
        	service = 'videopath',
        	thumbnail_large = 't1.jpg')
        ss = SourceSerializer(source)
        self.assertEqual(ss.data['service'],'videopath')
        self.assertEqual(ss.data['thumbnail_large'],settings.THUMBNAIL_CDN + 't1.jpg')


    def test_youtube_source(self):
        source = Source.objects.create(
        		service = 'youtube',
        		duration=100,
        		thumbnail_small = 'http://t1.jpg',
        		thumbnail_large = 'http://t2.jpg'
        	)
        ss = SourceSerializer(source)
        self.assertEqual(ss.data['thumbnail_small'],'http://t1.jpg')
        self.assertEqual(ss.data['thumbnail_large'],'http://t2.jpg')
        self.assertEqual(ss.data['service'],'youtube')