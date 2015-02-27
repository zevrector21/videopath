import requests


from django.core.management.base import BaseCommand
from django.conf import settings

from videopath.apps.common.services import service_provider

# constants
DUMPFILE = "./db_dump"
LATEST_BACKUP_URL = settings.PGBACKUPS_URL + "/latest_backup"

class Command(BaseCommand):

    def handle(self, *args, **options):

        # get latest backup info
        r = requests.get(LATEST_BACKUP_URL)
        dump_url = r.json()["public_url"]
        dump_timestamp = r.json()["finished_at"].replace("/", "-")
        dump_name = "videopath-api/" + dump_timestamp

        # write dump to file
        r = requests.get(dump_url, stream=True)
        if r.status_code == 200:
            with open(DUMPFILE, 'wb') as f:
                for chunk in r.iter_content():
                    f.write(chunk)

        # upload to s3
        s3_service = service_provider.get_service("s3")
        s3_service.upload(DUMPFILE, settings.AWS_DB_DUMPS_BUCKET, dump_name)
