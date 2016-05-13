from videopath.apps.users.models import User
from videopath.apps.payments.util import subscription_util

#
# Users User
#
def subscribe_to_plan(self, plan=None, coupon=None):
	return subscription_util.subscribe_user(self,plan,coupon)
User.subscribe_to_plan = classmethod(subscribe_to_plan)


def unsubscribe_from_plan(self):
	return subscription_util.unsubscribe_user(self)
User.unsubscribe_from_plan = classmethod(unsubscribe_from_plan)

