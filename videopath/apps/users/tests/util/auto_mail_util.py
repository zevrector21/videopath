from datetime import timedelta, datetime

from videopath.apps.common.test_utils import BaseTestCase
from videopath.apps.users.util import auto_mail_util
from videopath.apps.users.models import AutomatedMail

# Uses the standard django frame testing client
class TestCase(BaseTestCase):

    def setup(self):
        self.create_user()

    def test_creation(self):
    	
    	# a new user should not receive automails
        auto_mail_util.send_welcome_mails()
        self.assertEqual(AutomatedMail.objects.count(),0)

        # a user that joined over a week ago should
        self.user.date_joined = datetime.today() - timedelta(days=9)
        self.user.save()
        auto_mail_util.send_welcome_mails()
        self.assertEqual(AutomatedMail.objects.count(),1)
