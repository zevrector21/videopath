from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from videopath.apps.videos.models import PlayerAppearance
import shlex

from videopath.apps.videos.models import Video


accs = [
  'max@videopath.co',
  'max@videopath.com',
  'maxvideopath@gmail.com',
  'maximilianmealing@gmail.com',
  'anna@videopath.com',
  'anna2rose@gmail.com',
  'desiree@videopath.com',
  'adillon_88@hotmail.com',
  'louisa.denison@gmail.com',
  'tim@videopath.com'
]

class Command(BaseCommand):
    def handle(self, *args, **options):
    	count = 0
       	for v in Video.objects.filter(team__owner__email__in=accs):
       		count += 1
       		print count
       		v.player_version = '6'
       		v.save()

   		from videopath.apps.videos.util import video_export_util
    	video_export_util.export_all_videos(True)
	
