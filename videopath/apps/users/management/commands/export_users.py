from django.core.management.base import BaseCommand
from userena.models import UserenaSignup
from videopath.apps.videos.models import Video


class Command(BaseCommand):

    def handle(self, *args, **options):

    	users = {}
    	for v in Video.objects.all():
    		user = v.user
    		users[user.email] = {
    			user.email
    		}


    	for key, value in users.iteritems():
    		print key + ","

    	


