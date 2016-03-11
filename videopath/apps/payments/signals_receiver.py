from django.dispatch import receiver

from django.db.models.signals import post_save
from django.contrib.auth.models import User

from videopath.apps.analytics.signals import analytics_imported
from videopath.apps.payments.util import quota_util
from videopath.apps.vp_admin.signals import hourly_jobs
from videopath.apps.payments.util import payment_util, subscription_util

from videopath.apps.payments.models import Subscription

@receiver(analytics_imported)
def check_quotas(sender, **kwargs):
    quota_util.check_quotas()


@receiver(hourly_jobs)
def process_payments(sender, **kwargs):
    payment_util.process_payments()


@receiver(hourly_jobs)
def update_subscriptions(sender, **kwargs):
    subscription_util.update_subscriptions()

