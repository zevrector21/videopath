from django.core.management.base import BaseCommand


from django.conf import settings
logger = settings.LOGGER

class Command(BaseCommand):

    def handle(self, *args, **options):
        if settings.LOCAL:
            logger.warn("running locally not allowed")
            return
