from django.core.management.base import BaseCommand

from videopath.apps.videos.models import Source

class Command(BaseCommand):
    def handle(self, *args, **options):
       	for s in Source.objects.all():
       		s.sprite_support = False
       		s.save()
