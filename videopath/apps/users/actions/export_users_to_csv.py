from videopath.apps.videos.models import Video

def run():

	users = {}
	for v in Video.objects.all():
		user = v.user
		users[user.email] = {
			user.email
		}

	for key, value in users.iteritems():
		print key + ","

    	


