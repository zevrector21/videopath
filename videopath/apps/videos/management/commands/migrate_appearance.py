from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from videopath.apps.videos.models import PlayerAppearance
import shlex

from videopath.apps.videos.models import VideoRevision

def appearance_for_appearance(app):
		d = dict(token.split('=') for token in shlex.split(app))
		a = PlayerAppearance.objects.create()

		# transfer values
		a.ui_color_1 = d.get('ui_color_1', None)
		a.ui_color_2 = d.get('ui_color_2', None)
		a.icon = d.get('icon', None)
		a.endscreen_logo = d.get('endscreen_logo', None)
		a.sharing_disabled = d.get('sharing_disabled', False)
		a.language = d.get('language', 'en')
		a.save()

		return a

class Command(BaseCommand):
    def handle(self, *args, **options):
       	for r in VideoRevision.objects.all():
       		if r.video_appearance:
       			print r.title
       			print r.video_appearance
       			print "==="
       			print "==="
       			r.player_appearance=appearance_for_appearance(r.video_appearance)
       			r.player_appearance.description = r.title
    			r.player_appearance.save()
       			r.save()

       	for u in User.objects.all():
       		try:
	       		if u.settings.video_appearance:
	       			print u.username
	       			print u.settings.video_appearance
	       			u.default_player_appearance=appearance_for_appearance(u.settings.video_appearance)
	       			u.settings.save()
	       			u.default_player_appearance.save()
	       			print "==="
       				print "==="
	       	except:
	       		pass

	
