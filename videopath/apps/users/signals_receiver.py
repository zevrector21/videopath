from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from django.core.cache import cache

from django.contrib.auth.models import User

from videopath.apps.users.models import AuthenticationToken, Team
from videopath.apps.vp_admin.signals import hourly_jobs, daily_jobs

from videopath.apps.users.actions import sync_with_pipedrive
from videopath.apps.users.actions import expire_authentication_tokens
from videopath.apps.users.actions import clear_example_users
from videopath.apps.users.actions import send_welcome_mails
from videopath.apps.users.actions import send_follow_up_mails

@receiver(pre_delete, sender=AuthenticationToken)
def delete_auth_token_cache(sender, instance=None, **kwargs):
    cache.delete(instance.key + "-token")

@receiver(post_save, sender=User)
def create_default_team(sender, instance=None, **kwargs):
	 if instance:
	 	Team.objects.get_or_create(owner=instance, is_default_team_of_user=instance, name='My Projects')

@receiver(hourly_jobs)
def run_send_welcome_mails(sender, **kwargs):
    # send_welcome_mails.run()
    pass

@receiver(hourly_jobs)
def run_expire_authentication_tokens(sender, **kwargs):
    expire_authentication_tokens.run()

@receiver(hourly_jobs)
def run_send_follow_up_mails(sender, **kwargs):
    # send_follow_up_mails.run()
    pass

@receiver(daily_jobs)
def run_sync_with_pipedrive(sender, **kwargs):
	sync_with_pipedrive.run()

@receiver(daily_jobs)
def run_clear_example_users(sender, **kwargs):
	clear_example_users.run()