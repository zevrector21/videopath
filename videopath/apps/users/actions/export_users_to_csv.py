from django.contrib.auth.models import User

def run():

	for u in User.objects.all().order_by('-date_joined'):
		print u.email + ',' + str(u.date_joined.date())

    	


