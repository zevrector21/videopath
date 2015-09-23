from django.core.management.base import BaseCommand


from videopath.apps.videos.models import Video



class Command(BaseCommand):
    def handle(self, *args, **options):
       	for v in Video.objects.all():
       		v.ensure_draft()
	
