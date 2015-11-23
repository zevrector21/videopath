from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.cache import cache

from videopath.apps.users.models import AuthenticationToken
from videopath.apps.vp_admin.signals import hourly_jobs, daily_jobs

from videopath.apps.users.actions import sync_with_pipedrive
from videopath.apps.users.actions import expire_authentication_tokens
from videopath.apps.users.actions import clear_example_users
from videopath.apps.users.actions import send_welcome_mails


@receiver(pre_delete, sender=AuthenticationToken)
def delete_auth_token_cache(sender, instance=None, **kwargs):
    cache.delete(instance.key + "-token")

@receiver(hourly_jobs)
def run_send_welcome_mails(sender, **kwargs):
    send_welcome_mails.run()

@receiver(hourly_jobs)
def run_expire_authentication_tokens(sender, **kwargs):
    expire_authentication_tokens.run()

@receiver(daily_jobs)
def run_sync_with_pipedrive(sender, **kwargs):
	sync_with_pipedrive.run()

@receiver(daily_jobs)
def run_clear_example_users(sender, **kwargs):
	clear_example_users.run()