from django.core.management.base import BaseCommand


from videopath.apps.videos.models import Video
from videopath.apps.files.models import VideoSourceNew

class Command(BaseCommand):

    def handle(self, *args, **options):

    	count = 20
    	for v in Video.objects.all():
    		print "migrating " + str(v.pk)
    		self.migrate_video(v)
    		count-=1
    		if not count:
    			break


    def migrate_video(self, v):

    	# src = VideoSourceNew.objects.create()
    	# print "revisions "
    	source = None

    	try:
    		f = v.file.latest("created")
    		print "has file"
    	except:
    		pass

    	try:
    		s = v.video_sources.latest("created")
    		print "has source"
    	except:
    		pass
    	


    	if source:
    		for r in v.revisions.all():
    			r.source = source
    			r.save()
    			print "rev " + str(r.pk)
