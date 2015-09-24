#
# Generate source object until this is available later
#
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings


def source_for_video(v, vr = None):

	result = {
		'jpg_sequence_support': False
	}

	# if we have a sourceo object
	try:	
		video_source = v.video_sources.latest('created')
		result = {
			# basic
			'service': video_source.service,
			'service_identifier': video_source.service_identifier,

			# params
			'duration': video_source.video_duration,
			'aspect': video_source.video_aspect,

			# thumbs
			'thumbnail_small': video_source.thumbnail_url,
			'thumbnail_large': video_source.thumbnail_url,

			# files
			'file_mp4': video_source.source_mp4,
			'file_webm': video_source.source_webm,

			'status': 'ok',

			# special settings, might need to move out of here eventually
			'allow_youtube_clickthrough': video_source.allow_youtube_clickthrough

		}
	except ObjectDoesNotExist:
		pass

	# if we have a file object
	try:

		status_map = {
			-1:'error',
			0: 'awaiting_upload',
			1: 'processing',
			2: 'processing',
			3: 'processing',
			4: 'ok'
		}

		video_file = v.file.latest('created')
		result = {
			# basic
			'service': 'videopath',

			# params
			'duration': video_file.video_duration,
			'aspect': float(video_file.video_width) / float(video_file.video_height) if video_file.video_height else 0,

			# thumbs
			'thumbnail_small': '',
			'thumbnail_large': '',

			# files
			'file_mp4': settings.VIDEO_CDN + video_file.key + '.mp4',
			'file_webm': settings.VIDEO_CDN + video_file.key + '.webm',

			'status': status_map[video_file.status]
			
		}
	except ObjectDoesNotExist:
		pass

	# inject iphone playback info
	if vr and vr.iphone_images > 0:
		result.update({
			'jpg_sequence_support': True,
			'jpg_sequence_length': vr.iphone_images,
			'jpg_sequence_base_url': settings.JPGS_CDN + v.key + '/'
		})


	return result


def source_for_revision(rv):
	return source_for_video(rv.video, rv)
