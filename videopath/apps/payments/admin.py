from django.contrib import admin

from videopath.apps.payments.models import Subscription, PaymentDetails, StripeID, QuotaInformation, Payment, PendingSubscription
from videopath.apps.payments.util import payment_export_util

class StripeCustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'key')


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'paid', 'amount_due', 'number', 'download_url')
    def download_url(self, payment):
    	url = payment_export_util.url_for_payment(payment) 
    	return "<a href = '%s'>View</a>" % url
    download_url.allow_tags = True


class QuotaInformationAdmin(admin.ModelAdmin):
    list_display = ('user', 'quota_exceeded', 'warning_sent')


class StripeIDAdmin(admin.ModelAdmin):
    list_display = ('user', 'key')


class PaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ('user',)


class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'notes', 'active')
    search_fields = ['user__username', 'user__email']
    list_filter = ['plan', 'managed_by']


class PendingSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan')


admin.site.register(PaymentDetails, PaymentDetailsAdmin)
admin.site.register(Subscription, SubscriptionsAdmin)
admin.site.register(StripeID, StripeIDAdmin)
admin.site.register(QuotaInformation, QuotaInformationAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(PendingSubscription, PendingSubscriptionAdmin)
