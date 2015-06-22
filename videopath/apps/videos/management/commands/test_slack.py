from django.core.management.base import BaseCommand
from videopath.apps.common.services import service_provider

class Command(BaseCommand):
    def handle(self, *args, **options):
       	slack = service_provider.get_service("slack")
       	slack.notify("test message from api")

	
