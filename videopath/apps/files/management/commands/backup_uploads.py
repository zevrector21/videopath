from boto.s3.connection import S3Connection
from datetime import datetime,timedelta

from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):

    def handle(self, *args, **options):

        conn = S3Connection(
            settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        in_bucket = conn.get_bucket(settings.AWS_UPLOAD_BUCKET)
        backup_bucket = conn.get_bucket(settings.AWS_VIDEO_BACKUP_BUCKET)
        now = datetime.now()

        for key in in_bucket.list():

            backup_key = backup_bucket.get_key(key.name)
            if (backup_key):
                continue

            # if file is younger than one day, do not backup
            modified = datetime.strptime(
                key.last_modified[:19], "%Y-%m-%dT%H:%M:%S")
            if (now - modified < timedelta(days=1)):
                continue

            # if copy successfull, delete in in bucket
            result = key.copy(backup_bucket, key.name)
            if result:
                key.delete()
