from django.conf import settings

from videopath.apps.payments.models import Subscription

def run():

	usage_map = {}


	for p in settings.PLANS.all_plans:
		usage_map[p] = 0


	for s in Subscription.objects.all():
		usage_map[s.plan] += 1

	print 'Plan by usage'
	print '=='
	for k,v in usage_map.iteritems():
		print k + ': '+str(v)

		if v < 30:
			for s in Subscription.objects.filter(plan=k):
				print s.user.username + ' // ' + s.user.email

		print '-'






