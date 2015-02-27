from django.core.management.base import BaseCommand

from videopath.apps.files.aws import delete_orphaned_files

from django.conf import settings
logger = settings.LOGGER

class Command(BaseCommand):

    def handle(self, *args, **options):
        if settings.LOCAL:
            logger.warn("running locally not allowed")
            return
        delete_orphaned_files()
