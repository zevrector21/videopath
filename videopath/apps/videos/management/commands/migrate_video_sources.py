from django.core.management.base import BaseCommand
from videopath.apps.videos.models import Video, Source
from django.core.exceptions import ObjectDoesNotExist

from django.conf import settings
from videopath.apps.files.util import thumbnails_util

status_map = {
			-1:'error',
			0: 'awaiting_upload',
			1: 'processing',
			2: 'processing',
			3: 'processing',
			4: 'ok'
		}



#
# Convert old file object
#
def convert_file(file):
	cdn_path = settings.THUMBNAIL_CDN 

	return Source.objects.create(
		service = 'videopath',
		key = file.key,
		status = status_map[file.status],
		duration = file.video_duration,
		aspect = float(file.video_width) / float(file.video_height) if file.video_height else 0,
		file_mp4 = file.key + '.mp4',
		file_webm = file.key + '.webm',
		thumbnail_large = thumbnails_util.large_thumbnail_url_for_videofile(file).replace(cdn_path, ''),
		thumbnail_small = thumbnails_util.thumbnail_url_for_videofile(file).replace(cdn_path, '')
		)

#
# Convert old source object to new source object
#
def convert_source(src):
	return Source.objects.create(
		status = 'ok',
		service = src.service,
		service_identifier = src.service_identifier,
		aspect = src.video_aspect,
		duration = src.video_duration,
		thumbnail_large = src.thumbnail_url,
		thumbnail_small = src.thumbnail_url,
		file_mp4 = src.source_mp4,
		file_webm = src.source_webm,
		youtube_allow_clickthrough = src.allow_youtube_clickthrough,
		description=src.title
		)

#
# 
#
class Command(BaseCommand):
    def handle(self, *args, **options):

    	for s in Source.objects.all():
    		s.delete()

    	empty_video_count = 0
    	no_source_count = 0

       	for v in Video.objects.all():
			source = None

			try:
				video_file = v.file.latest('created')
				source = convert_file(video_file)
			except ObjectDoesNotExist:
				pass

			try:
				video_source = v.video_sources.latest('created')
				source = convert_source(video_source)
			except ObjectDoesNotExist:
				pass

			if v.file.count() == 0 and v.video_sources.count() == 0:
				empty_video_count+=1

			if not source:
				no_source_count += 1

			if v.file.count() > 0 and v.video_sources.count() > 0:
				print v.key

			if source and v.draft_id:
				v.draft.source = source
				v.draft.save()
				if v.draft.iphone_images > 0:
					source.jpg_sequence_support = True
					source.jpg_sequence_length = v.draft.iphone_images
					source.save()
					print "jpg migrate: " + v.key + " -> " + source.key


			if source and v.current_revision_id:
				v.current_revision.source = source
				v.current_revision.save()


       	print "videos: " + str(Video.objects.count())
       	print "sources: " + str(Source.objects.count())
       	print "empty vids: " + str(empty_video_count)
       	print "no source: " + str(no_source_count)


	
