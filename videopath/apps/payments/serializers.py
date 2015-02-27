from rest_framework import serializers

from django.conf import settings

from videopath.apps.payments.models import PaymentDetails, Subscription, Payment, PendingSubscription
from videopath.apps.payments.util import payment_export_util, usage_util

#
# Serialize plans
#
class PlanSerializer(serializers.Serializer):

    # id
    id = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200)
    group = serializers.CharField(max_length=200)

    # payment details
    payment_interval = serializers.CharField(max_length=200)
    price_eur = serializers.IntegerField()

    # plan contraints
    max_views_month = serializers.IntegerField()
    max_projects = serializers.IntegerField()

    # features
    feature_upload = serializers.BooleanField()
    feature_analytics = serializers.BooleanField()
    feature_endscreen = serializers.BooleanField()
    feature_vimeo = serializers.BooleanField()
    feature_colors = serializers.BooleanField()
    feature_dev = serializers.BooleanField()
    feature_disable_share = serializers.BooleanField()
    feature_equal_markers = serializers.BooleanField()

#
# Serialize CreditCards
#
class CreditCardSerializer(serializers.Serializer):

    last4 = serializers.CharField(max_length=200)
    exp_month = serializers.IntegerField()
    exp_year = serializers.IntegerField()

#
# Payment Details / Address
#
class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = ('name', 'street', 'city', 'post_code', 'country')

#
# Payment / Invoices
#
class PaymentSerializer(serializers.ModelSerializer):

    download_url = serializers.SerializerMethodField()

    def get_download_url(self, payment):
        return payment_export_util.url_for_payment(payment)

    class Meta:
        model = Payment
        fields = ('amount_due', 'date', 'paid', 'number', 'download_url')
        readonly_fields = ('amount_due', 'date', 'paid', 'number')

#
# Actual subscription
#
class SubscriptionSerializer(serializers.ModelSerializer):

    plan = serializers.SerializerMethodField()

    pending_subscription = serializers.SerializerMethodField()

    current_month_views = serializers.SerializerMethodField()

    def get_current_month_views(self, subscription):
        return usage_util.plan_usage_current(subscription.user)

    def get_plan(self, subscription):
        plan = settings.PLANS.plan_for_id(subscription.plan)
        return PlanSerializer(plan).data

    def get_pending_subscription(self, subscription):
        try:
            plan = settings.PLANS.plan_for_id(subscription.user.pending_subscription.plan)
            return PlanSerializer(plan).data
        except PendingSubscription.DoesNotExist:
            return False


    class Meta:
        model = Subscription
        fields = ( 'current_period_start', 'current_period_end', 'current_month_views', 'plan', 'pending_subscription')
        read_only_fields = ( 'plan','current_period_start', 'current_period_end')
