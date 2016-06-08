from videopath.apps.users.models import User
from videopath.apps.payments.util import subscription_util
from types import MethodType

#
# Users User
#
def subscribe_to_plan(self, plan=None, coupon=None):
	print self
	return subscription_util.subscribe_user(self,plan,coupon)
User.subscribe_to_plan = MethodType(subscribe_to_plan, None, User)


def unsubscribe_from_plan(self):
	return subscription_util.unsubscribe_user(self)
User.unsubscribe_from_plan = MethodType(unsubscribe_from_plan, None, User)

