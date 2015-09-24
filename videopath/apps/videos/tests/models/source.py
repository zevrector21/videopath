
from videopath.apps.videos.models import Source
from videopath.apps.common.test_utils import BaseTestCase

# Uses the standard django frame testing client
class TestCase(BaseTestCase):

    def setup(self):
        self.create_user()

    def test_creation(self):
        # video should be creatable 
        source = Source.objects.create()



