from videopath.apps.payments.models import Subscription

def run(user):
	try:
		user.pending_subscription.delete()
	except: pass
	user.subscription.delete()
	Subscription.objects.create(user=user)