from django.core.management.base import BaseCommand
from videopath.apps.videos.models import Video, VideoSource


def convert_file(file):
	return VideoSource.objects.create()

def convert_source(file):
	return VideoSource.objects.create()

class Command(BaseCommand):
    def handle(self, *args, **options):
       	for v in Video.objects.all():
       		pass

       	print "videos: " + str(Video.objects.count())
       	print "sources: " + str(VideoSource.objects.count())


	
