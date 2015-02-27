from boto.s3.connection import S3Connection

from django.core.management.base import BaseCommand
from django.conf import settings

from videopath.apps.files.models import VideoFile

class Command(BaseCommand):

    def handle(self, *args, **options):

        conn = S3Connection(
            settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        in_bucket = conn.get_bucket(settings.AWS_UPLOAD_BUCKET)
        backup_bucket = conn.get_bucket(settings.AWS_VIDEO_BACKUP_BUCKET)
        transcode_bucket = conn.get_bucket(settings.AWS_VIDEOS_BUCKET)

        files = VideoFile.objects.filter(transcoded_bytes=0)

        for f in files:

            if f.status == VideoFile.CREATED:
                continue

            # get original bytes
            if f.original_bytes == 0:
                in_key = in_bucket.get_key(f.key)
                if not in_key:
                    in_key = backup_bucket.get_key(f.key)
                if not in_key:
                    continue
                f.original_bytes = in_key.size

            # get transcoded bytes
            transcoded_size = 0
            exts = ["mp4", "webm"]
            for ext in exts:
                transcoded_key = transcode_bucket.get_key(f.key + "." + ext)
                if transcoded_key:
                    transcoded_size += transcoded_key.size

            f.transcoded_bytes = transcoded_size

            f.save()
