from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from videopath.apps.videos.models import PlayerAppearance
import shlex

from videopath.apps.videos.models import Video



class Command(BaseCommand):
    def handle(self, *args, **options):
       	for v in Video.objects.all():
       		v.player_version = ''
       		v.save()

   		from videopath.apps.videos.util import video_export_util
    	video_export_util.export_all_videos(True)
	
