FREE_PLAN = 'free-free'
EVALUATION_PLAN = 'individual-agency-evaluation'
EVALUATION_PERIOD_WEEKS = 4

from videopath.apps.payments.models import PendingSubscription
from datetime import date, timedelta

def run(user):
	if user.subscription.plan != FREE_PLAN and user.subscription.plan != EVALUATION_PLAN:
		return
	
	user.subscription.plan = EVALUATION_PLAN
	user.subscription.current_period_start = date.today()
	user.subscription.current_period_end = date.today() + timedelta(weeks=EVALUATION_PERIOD_WEEKS)
	user.subscription.save()

	PendingSubscription.objects.create(user=user, plan=FREE_PLAN)

