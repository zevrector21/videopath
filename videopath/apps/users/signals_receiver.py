from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.cache import cache
from django.core.management import call_command

from videopath.apps.users.models import AuthenticationToken
from videopath.apps.vp_admin.signals import hourly_jobs, daily_jobs

from videopath.apps.users.actions import sync_with_pipedrive

# delete files on s3 if file object is deleted


@receiver(pre_delete, sender=AuthenticationToken)
def delete_auth_token_cache(sender, instance=None, **kwargs):
    cache.delete(instance.key + "-token")

@receiver(hourly_jobs)
def send_automatic_mails(sender, **kwargs):
    call_command("send_automatic_mails")

@receiver(hourly_jobs)
def send_(sender, **kwargs):
    call_command("expire_authentication_tokens")

@receiver(daily_jobs)
def run_sync_with_pipedrive(sender, **kwargs):
	sync_with_pipedrive.run()
