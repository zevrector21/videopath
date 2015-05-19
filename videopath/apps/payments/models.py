from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from videopath.apps.common.models import VideopathBaseModel

#
# Remember stripe id of user
#
class StripeID(VideopathBaseModel):
    # stripe id
    key = models.CharField(max_length=50, unique=True, db_index=True)

    # user ref
    user = models.OneToOneField(User,
                                primary_key=True,
                                unique=True,
                                verbose_name=('user'),
                                related_name='stripe_id')

#
# Payment details of user, the adress
#
COUNTRY_CHOICES = settings.COUNTRIES_TUPLES()
class PaymentDetails(VideopathBaseModel):

    # data
    name = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    post_code = models.CharField(max_length=150)
    country = models.CharField(max_length=150, choices=COUNTRY_CHOICES)

    # user ref
    user = models.OneToOneField(User,
                                primary_key=True,
                                unique=True,
                                verbose_name=('user'),
                                related_name='payment_details')

#
# keeping track of quota usage of a user
#
class QuotaInformation(VideopathBaseModel):

    quota_exceeded = models.BooleanField(default=False)
    warning_sent = models.BooleanField(default=False)

    user = models.OneToOneField(User,
                                primary_key=True,
                                unique=True,
                                verbose_name=('user'),
                                related_name='quota_info')

#
# Payments charged to the user, one payment is one invoice, should probably be renamed
#
class Payment(VideopathBaseModel):

    PROVIDER_OTHER = "other"
    PROVIDER_STRIPE = "stripe"
    PROVIDER_TRANSFER = "transfer"
    PROVIDER_CHOICES = (
        (PROVIDER_OTHER, PROVIDER_OTHER),
        (PROVIDER_STRIPE, PROVIDER_STRIPE),
        (PROVIDER_TRANSFER, PROVIDER_TRANSFER)
    )

    # meta
    exported_invoice = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    charging_attempts = models.IntegerField(default=0)
    last_charging_attempt = models.DateField(null=True)
    provider = models.CharField(
        max_length=150, choices=PROVIDER_CHOICES, default=PROVIDER_OTHER)
    transaction_id = models.CharField(max_length=150, default="")

    # content
    amount_due = models.IntegerField(default=0)
    percent_vat = models.IntegerField(default=0)
    date = models.DateTimeField(null=True, auto_now_add=True)
    number = models.IntegerField(default=0)

    # the currency in which this payment/invoice is issued
    currency = models.CharField(
        max_length=3, default=settings.CURRENCY_EUR, choices=settings.CURRENCY_CHOICES)

    # serialized json with all the lines in the payment
    details = models.CharField(max_length=2048)

    # user
    user = models.ForeignKey(User, related_name='payments')

    # set number
    def save(self, *args, **kwargs):
        if self.number == 0:
            highest = settings.INVOICE_START_NUMBER
            try:
                latest = Payment.objects.latest('number')
                highest = latest.number
            except:
                pass
            self.number = highest + 1
        super(Payment, self).save(*args, **kwargs)

#
# Subscriptions, which plan the user is currently subscribed to
#
SUBSCRIPTION_CHOICES = settings.PLANS.model_subscription_choices()

class Subscription(VideopathBaseModel):

    MANAGER_ADMIN = "admin"
    MANAGER_STRIPE = "stripe"
    MANAGER_SYSTEM = "system"

    MANAGER_CHOICES = (
        (MANAGER_ADMIN, MANAGER_ADMIN),
        (MANAGER_STRIPE, MANAGER_STRIPE),
        (MANAGER_SYSTEM, MANAGER_SYSTEM),
    )

    plan = models.CharField(
        max_length=150, choices=SUBSCRIPTION_CHOICES, default=settings.PLANS.default_plan["id"])
    active = models.BooleanField(default=True)

    # meta
    managed_by = models.CharField(
        max_length=255, choices=MANAGER_CHOICES, default=MANAGER_ADMIN)

    # detailed information
    current_period_start = models.DateField(null=True, blank=True)
    current_period_end = models.DateField(null=True, blank=True)

    # custom price
    price = models.IntegerField(default=-1)
    currency = models.CharField(
        max_length=3, default=settings.CURRENCY_EUR, choices=settings.CURRENCY_CHOICES)

    # user ref
    user = models.OneToOneField(User,
                                primary_key=True,
                                unique=True,
                                verbose_name=('user'),
                                related_name='subscription')

    # notes for internal use
    notes = models.TextField(default="")

#
# pending subscription, if the user has changed his plan,
# but needs to stay in the current one until it expires
#
class PendingSubscription(VideopathBaseModel):

    plan = models.CharField(max_length=150, choices=SUBSCRIPTION_CHOICES)

    user = models.OneToOneField(User,
                                primary_key=True,
                                unique=True,
                                verbose_name=('user'),
                                related_name='pending_subscription')
