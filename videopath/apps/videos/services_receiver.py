from videopath.apps.common.services import service_provider
from videopath.apps.common import mailer

from videopath.apps.videos.models import Source


service = service_provider.get_service("services")

#
# Called when there was an error transcoding a videos to jpgs
#
def jpg_transcode_error(message):
	key = message['api_command']['source']['key']
	try:
		source = Source.objects.get(key=key)
		for v in source.get_attached_videos():
			mailer.send_jpgs_trancode_failed_mail(v)
	except Source.DoesNotExist:
		pass 

service.receive_messages('q-transcoder-errors', jpg_transcode_error)

#
# Called when there was a success transcoding videos to jpgs
#
def jpg_transcode_success(message):
	key = message['key']
	try:

		# update source object
		source = Source.objects.get(key=key)
		source.jpg_sequence_support = True
		source.jpg_sequence_length = message['results']['frames']
		source.save()

		# reexport all attached video objects
		for v in source.get_attached_videos():
			v.reexport()
			mailer.send_jpgs_trancode_succeeded_mail(v)

	except Source.DoesNotExist:
		pass # do nothing..
		
service.receive_messages('q-transcoder-results', jpg_transcode_success)