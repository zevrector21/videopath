from django.core.management.base import BaseCommand
from videopath.apps.videos.models import Video, VideoSource


def convert_file(file):
	return VideoSource.objects.create()

def convert_source(file):
	return VideoSource.objects.create()

class Command(BaseCommand):
    def handle(self, *args, **options):
       	for v in Video.objects.all():
			source = None

			try:
				video_file = v.file.latest('created')
				source = convert_file(video_file)
			except:
				pass

			try:
				video_source = v.video_sources.latest('created')
				source = convert_source(video_source)
			except:
				pass


			if source and v.draft_id:
				v.draft.source = source
				v.draft.save()
			if source and v.current_revision_id:
				v.current_revision.source = source
				v.current_revision.save()


       	print "videos: " + str(Video.objects.count())
       	print "sources: " + str(VideoSource.objects.count())


	
