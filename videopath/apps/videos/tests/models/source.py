
from videopath.apps.videos.models import Source
from videopath.apps.common.test_utils import BaseTestCase

# Uses the standard django frame testing client
class TestCase(BaseTestCase):

    def setup(self):
        self.create_user()

    def test_creation(self):
        # source should be creatable 
        Source.objects.create()

    def test_jpgs_export(self):
    	source = Source.objects.create({
    		'service': 'youtube',
    		'service_identifier': '092834sdf'
    		})
    	source.export_jpgs()



