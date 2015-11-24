from datetime import timedelta, datetime

from django.contrib.auth.models import User

from videopath.apps.common import mailer
from videopath.apps.users.models import AutomatedMail

TREE_WEEKS = 21
SIX_WEEKS = 42	
TWO_MONTHS = 70
DEFAULT_MAX_MAILS = 10

def run(max_mails=DEFAULT_MAX_MAILS):
	_send_three_weeks_follow_up(max_mails)
	_send_six_weeks_follow_up(max_mails)


def _send_three_weeks_follow_up(max_mails):
	three_weeks_ago = datetime.now() - timedelta(days=TREE_WEEKS)
	two_months_ago = datetime.now() - timedelta(days=TWO_MONTHS)

	# all users which have received mail 21 and have not been seen for longer than 3 weeks
	users = User.objects.filter(activity__last_seen__lte=three_weeks_ago, date_joined__gte=two_months_ago)
	users = users.exclude(automated_mails__mailtype=AutomatedMail.TYPE_FOLLOW_UP_21)

	count = 0
	for u in users:
		# send
		AutomatedMail.objects.create(user=u, mailtype = AutomatedMail.TYPE_FOLLOW_UP_21)
		count += 1
		if count > max_mails: break

def _send_six_weeks_follow_up(max_mails):
	six_weeks_ago = datetime.now() - timedelta(days=SIX_WEEKS)
	two_months_ago = datetime.now() - timedelta(days=TWO_MONTHS)

	# all users which have received mail 21 and have not been seen for longer than 6 weeks
	users = User.objects.filter(activity__last_seen__lte=six_weeks_ago,  date_joined__gte=two_months_ago, automated_mails__mailtype = AutomatedMail.TYPE_FOLLOW_UP_21)
	users = users.exclude(automated_mails__mailtype=AutomatedMail.TYPE_FOLLOW_UP_42)

	count = 0
	for u in users:
		three_weeks_ago = datetime.now() - timedelta(days=TREE_WEEKS)
		if u.automated_mails.filter(mailtype=AutomatedMail.TYPE_FOLLOW_UP_21, created__gte=three_weeks_ago).count():
			continue
		# send
		AutomatedMail.objects.create(user=u, mailtype = AutomatedMail.TYPE_FOLLOW_UP_42)
		count += 1
		if count > max_mails: break