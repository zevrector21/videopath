from django.db import models
from django.contrib.auth.models import User as _User

from userena.models import UserenaBaseProfile

from videopath.apps.common.models import VideopathBaseModel
from django.conf import settings

#
# Proxy model for users, so that we can add stuff to it
#
class User(_User):
    def reload(self):
        return self.__class__.objects.get(pk=self.pk)
    class Meta:
        proxy = True
    def __unicode__(self):
        return self.email + " - " + self.username

#
# All the users settings go here
#
class UserSettings(UserenaBaseProfile):

    user = models.OneToOneField(_User,
                                unique=True,
                                verbose_name=('user'),
                                related_name='settings')

    currency = models.CharField(
        max_length=3, default=settings.CURRENCY_EUR, choices=settings.CURRENCY_CHOICES)
    payment_provider = models.CharField(
        max_length=150, default=settings.PAYMENT_PROVIDER_STRIPE, choices=settings.PAYMENT_PROVIDER_CHOICES)
    phone_number = models.CharField(
        max_length=100, default='')

    class Meta:
        verbose_name = 'User Settings'
        verbose_name_plural = 'User Settings'

    def __unicode__(self):
        return "Settings of " + self.user.__unicode__() 

#
# Campaign Data to store info about where the user came from
#
class UserCampaignData(VideopathBaseModel):
    user = models.OneToOneField(_User, 
                                unique=True, 
                                verbose_name=('user'),
                                related_name='campaign_data'
                                )

    # utm terms
    source = models.CharField(max_length=512, default='', null=True)
    medium = models.CharField(max_length=512, default='', null=True)
    name = models.CharField(max_length=512, default='', null=True)
    content = models.CharField(max_length=512, default='', null=True)
    term = models.CharField(max_length=512, default='', null=True)

    # other info
    country = models.CharField(max_length=512, default='', null=True)
    referrer = models.CharField(max_length=512, default='', null=True)

#
# SalesInfo, saves connection to crm (pipedrive atm)
#
class UserSalesInfo(VideopathBaseModel):
    user = models.OneToOneField(_User, 
                                unique=True, 
                                verbose_name=('user'),
                                related_name='sales_info'
                                )
    pipedrive_person_id = models.IntegerField(default=-1, null=True)


#
# remember when users have last been seen
#
class UserActivity(VideopathBaseModel):

    user = models.OneToOneField(_User,
                                unique=True,
                                verbose_name=('user'),
                                related_name='activity')
    last_seen = models.DateTimeField(blank=True, null=True)

#
# remember days on which users where logged in
#
class UserActivityDay(VideopathBaseModel):
    user = models.ForeignKey(_User, related_name="user_activity_day")
    day = models.DateField(auto_now_add=True)
    class Meta:
        unique_together = ("user", "day")

#
# track marketing mails sent to users
#
class AutomatedMail(VideopathBaseModel):

    TYPE_WELCOME = "welcome"
    TYPE_FOLLOW_UP_21 = "follow_up_21"
    TYPE_FOLLOW_UP_42 = "follow_up_42"

    TYPE_CHOICES = (
        (TYPE_WELCOME, TYPE_WELCOME),
        (TYPE_FOLLOW_UP_21, TYPE_FOLLOW_UP_21),
        (TYPE_FOLLOW_UP_42, TYPE_FOLLOW_UP_42),
    )
    user = models.ForeignKey(_User, related_name="automated_mails")
    mailtype = models.CharField(
        max_length=20, choices=TYPE_CHOICES, default="")

#
# List of authentication tokens given out to users
#
class AuthenticationToken(VideopathBaseModel):

    user = models.ForeignKey(_User, related_name="authentication_tokens")
    key = models.CharField(max_length=40, primary_key=True)
    last_used = models.DateTimeField(auto_now_add=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key(32)
        return super(AuthenticationToken, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.key

#
# One time authentication tokens, useful in certain conditions, for example our
# annoying http to https switch on the frontend
#
class OneTimeAuthenticationToken(VideopathBaseModel):

    token = models.ForeignKey(
        AuthenticationToken, related_name="onetime_tokens")
    key = models.CharField(max_length=40, primary_key=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key(32)
        return super(OneTimeAuthenticationToken, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.key
