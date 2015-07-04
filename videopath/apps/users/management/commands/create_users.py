from django.core.management.base import BaseCommand
from userena.models import UserenaSignup

import sys

class Command(BaseCommand):

    def handle(self, *args, **options):

    	print sys.argv

    	amount = 60

    	while amount > 50:
    		

			username = "student-" + str(amount) + "@videopath.com"
			password = "videopath-"+ str(amount)

			user = UserenaSignup.objects.create_user(username,
			                             username,
			                             password,
			                             active=True, send_email=False)
			amount-=1


