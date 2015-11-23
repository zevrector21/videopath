from datetime import timedelta, datetime

from django.contrib.auth.models import User

from videopath.apps.common import mailer
from videopath.apps.users.models import AutomatedMail

USER_MIN_AGE_IN_DAYS = 7
DEFAULT_MAX_MAILS = 10

def run(max_mails=DEFAULT_MAX_MAILS):
	thresh = datetime.now() - timedelta(days=USER_MIN_AGE_IN_DAYS)
	users = User.objects.filter(date_joined__lte=thresh, sales_info__exact = None)
	users = users.exclude(automated_mails__mailtype=AutomatedMail.TYPE_WELCOME)
	count = 0
	for u in users:
	    _send_welcome_mail(u)
	    count += 1
	    if count >= max_mails: break

def _send_welcome_mail(user):
    mailer.send_welcome_mail(user)
    AutomatedMail.objects.create(mailtype=AutomatedMail.TYPE_WELCOME, user=user)