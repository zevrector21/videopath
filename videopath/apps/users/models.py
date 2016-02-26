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
# Proxy user model for Sales list
#
class UserSales(_User):
    class Meta:
        proxy = True

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

    # email settings
    receive_system_emails = models.BooleanField(default=True)
    receive_retention_emails = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'User Settings'
        verbose_name_plural = 'User Settings'

    def __unicode__(self):
        return "Settings of " + self.user.__unicode__() 


#
# Team model, all videos are organized beneath a team
#
class Teams(models.Manager):

    def teams_for_user(self, user):
        return self.filter(models.Q(owner = user) | models.Q(members = user)  )

class Team(VideopathBaseModel):

    objects = Teams()

    owner = models.ForeignKey(_User, related_name='owned_teams')
    name = models.CharField(max_length=150, default='My Projects')
    members = models.ManyToManyField(_User, through='TeamMember')

    # each user has a default team where his projects go
    # this is defined on team, as the django user object is 
    # not really mutable
    is_default_team_of_user = models.OneToOneField(_User,
                                                unique=True,
                                                verbose_name=('default_team_of_user'),
                                                related_name='default_team',
                                                null=True,
                                                blank=True)

    def is_a_default_team(self):
        return self.is_default_team_of_user != None

    def add_member(self, user, role=None):
        if not role: role = 'editor'
        if self.is_a_default_team() or user == self.owner:
            return
        member, created = TeamMember.objects.get_or_create(team=self, user=user, role=role)
        return member

    def remove_member(self,user):
        try:
            member = TeamMember.objects.get(team=self, user=user)
            member.delete()
        except TeamMember.DoesNotExist: pass

    def is_user_member(self, user):
        return user in self.members.all() or user == self.owner

    def is_user_admin(self, user):
        if user == self.owner: return True
        return TeamMember.objects.filter(user=user, team=self, role='admin').count() > 0

    def is_user_owner(self, user):
        return self.owner == user

    def can_be_deleted(self):
        return not self.videos.count() > 0 and not self.is_a_default_team()

    def delete(self):
        if self.can_be_deleted(): super(Team, self).delete()

    def __unicode__(self):
        if self.is_a_default_team():
            return "Default team ({0})".format(self.is_default_team_of_user.email)
        return "Team {0} ({1})".format(self.name, self.owner)




#
# Team member, connects people to teams
#
class TeamMembers(models.Manager):

    def filter_for_user(self, user):
        return self.filter(models.Q(team__owner = user) | models.Q(team__members = user)  )

class TeamMember(VideopathBaseModel):

    objects = TeamMembers()

    ROLE_EDITOR = "editor"
    ROLE_ADMIN = "admin"

    TYPE_CHOICES = (
        (ROLE_EDITOR, ROLE_EDITOR),
        (ROLE_ADMIN, ROLE_ADMIN),
    )

    team = models.ForeignKey(Team)
    user = models.ForeignKey(_User)
    role = models.CharField(max_length=20, choices=TYPE_CHOICES, default=ROLE_EDITOR)

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
