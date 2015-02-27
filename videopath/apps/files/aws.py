from django.conf import settings

from videopath.apps.common.services import service_provider

logger = settings.LOGGER

s3_service = service_provider.get_service("s3")
elastic_transcoder_service = service_provider.get_service("elastic_transcoder")

def get_upload_endpoint_for_video(expires_in=6000, key=None, method='POST'):

    #conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)

    #bucket = conn.get_bucket(settings.AWS_UPLOAD_BUCKET, validate = False)
    #key = bucket.new_key(key)
    #url = key.generate_url(1000, method='POST', force_http = True, headers={'Content-Length': '1475821'})
    #url = conn.generate_url(300, 'PUT', settings.AWS_UPLOAD_BUCKET, key, headers={'Content-Length': '19448423'}, force_http = True )
    #form = conn.build_post_form_args(bucket_name=settings.AWS_UPLOAD_BUCKET, key=key, expires_in=expires_in)

    # for now we return an unsigned url
    url = "https://" + settings.AWS_UPLOAD_BUCKET + ".s3.amazonaws.com"

    return url


def get_upload_endpoint_for_image(expires_in=6000, key=None, method='POST'):
    url = "https://" + settings.AWS_UPLOAD_BUCKET + ".s3.amazonaws.com"
    return url


def verify_video_upload(ticket_id=None):
    return s3_service.check_existence(settings.AWS_UPLOAD_BUCKET, ticket_id)


def verify_image_upload(ticket_id=None):
    return s3_service.check_existence(settings.AWS_UPLOAD_BUCKET, ticket_id)


def start_transcoding_video(video):
    logger.info('start_transcoding_video')

    t_input = {
        'Key': video.key,
        'FrameRate': 'auto',
        'Resolution': 'auto',
        'AspectRatio': 'auto',
        'Interlaced': 'auto',
        'Container': 'auto',
    }

    composition = [{
        'TimeSpan': {
            'StartTime': '00000.000',
            'Duration': '00600.000',  # 10 minutes limit on clips
        }
    }]

    t_output_mp4 = {
        'Key': video.key + '.mp4',
        'ThumbnailPattern': video.key + '/{count}-hd',
        'Rotate': 'auto',
        'PresetId': settings.AWS_TRANSCODE_PRESET_ID,
        'Composition': composition,
    }

    t_ouput_webm = {
        'Key': video.key + '.webm',
        'ThumbnailPattern': video.key + '/{count}',
        'Rotate': 'auto',
        'PresetId': settings.AWS_TRANSCODE_PRESET_ID2,
        'Composition': composition,
    }

    return elastic_transcoder_service.start_transcoding_job(t_input, None, [t_output_mp4, t_ouput_webm])


def delete_video_files_for_key(file_key):

    # delete file from in bucket
    s3_service.delete(settings.AWS_UPLOAD_BUCKET, file_key)

    # delete from out bucket
    for key in s3_service.list_keys(settings.AWS_VIDEOS_BUCKET, prefix = file_key):
        s3_service.delete(settings.AWS_VIDEOS_BUCKET, key)

    # delete from thumbs bucket
    for key in s3_service.list_keys(settings.AWS_THUMBNAIL_BUCKET, prefix = file_key):
        s3_service.delete(settings.AWS_THUMBNAIL_BUCKET, key)


def delete_image_files_for_key(file_key):
    s3_service.delete(settings.AWS_UPLOAD_BUCKET, file_key)
    s3_service.delete(settings.AWS_IMAGE_OUT_BUCKET, file_key)


def confirm_subscription(topic, token):
    logger.info('\confirm_subscription\n')
    return elastic_transcoder_service.confirm_subscription_topic(topic, token)


def delete_orphaned_files():
    pass
    # disabled for now, code needs review
    # return
    # conn = S3Connection(
    #     settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)

    # bucket = conn.get_bucket(settings.AWS_UPLOAD_BUCKET, validate=False)
    # for key in bucket.list():
    #     if not videofile_with_key_exists(key.name):
    #         bucket.delete_key(key)
    #         logger.info("deleting orphaned file " + key.name)

    # bucket = conn.get_bucket(settings.AWS_VIDEOS_BUCKET, validate=False)
    # for key in bucket.list():
    #     name = key.name
    #     name = split(r'[./]+', name)[0]
    #     if not videofile_with_key_exists(name):
    #         bucket.delete_key(key)
    #         logger.info("deleting orphaned file " + key.name)

    # bucket = conn.get_bucket(settings.AWS_THUMBNAIL_BUCKET, validate=False)
    # for key in bucket.list():
    #     name = key.name
    #     name = split(r'[./]+', name)[0]
    #     if not videofile_with_key_exists(name):
    #         bucket.delete_key(key)
    #         logger.info("deleting orphaned file " + key.name)
