from django.contrib import admin

from videopath.apps.payments.models import Subscription, PaymentDetails, StripeID, QuotaInformation, Payment, PendingSubscription

class StripeCustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'key')


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'paid', 'amount_due', 'number')


class QuotaInformationAdmin(admin.ModelAdmin):
    list_display = ('user', 'quota_exceeded', 'warning_sent')


class StripeIDAdmin(admin.ModelAdmin):
    list_display = ('user', 'key')


class PaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ('user',)


class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'active')


class PendingSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan')


admin.site.register(PaymentDetails, PaymentDetailsAdmin)
admin.site.register(Subscription, SubscriptionsAdmin)
admin.site.register(StripeID, StripeIDAdmin)
admin.site.register(QuotaInformation, QuotaInformationAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(PendingSubscription, PendingSubscriptionAdmin)
