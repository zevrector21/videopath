from django.core.management.base import BaseCommand

from videopath.apps.payments import quota_manager

class Command(BaseCommand):

    def handle(self, *args, **options):
        quota_manager.check_quotas()
