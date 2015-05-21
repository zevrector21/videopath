import json

from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response

from videopath.apps.files.models import VideoFile
from videopath.apps.files.util.aws_util import confirm_subscription
from videopath.apps.common.mailer import send_transcode_failed_mail, send_transcode_succeeded_mail

from django.conf import settings
logger = settings.LOGGER


@api_view(['POST', 'DELETE'])
@permission_classes((AllowAny,))
def process_notification(request, notification_type=None):

    try:
        post = request.data
    except BaseException:
        logger.error('Could not interpret notification message')
        return Response()

    # respond to aws subscription request
    if post['Type'] == 'SubscriptionConfirmation':
        logger.info('\Processing SubscriptionConfirmation\n')
        if 'Token' in post and 'TopicArn' in post:
            confirm_subscription(post['TopicArn'], post['Token'])
            logger.info('\nSubscriptionConfirmation\n')
            return Response()

    # retrieve video file
    message = json.loads(post['Message'])
    key = message['input']['key']

    try:
        vfile = VideoFile.objects.get(key=key)
    except VideoFile.DoesNotExist:
        logger.warn(
            "Received transcoding notification for file that does not exist :" + key)
        return Response()

    # parse status out of type
    if notification_type == 'progressing':
        vfile.status = VideoFile.TRANSCODING_STARTED
        logger.info('Video changed to TRANSCODING_STARTED: %s' %
                    (vfile.video.key))

    elif notification_type == 'complete':
        vfile.video_width = message['outputs'][0]['width']
        vfile.video_height = message['outputs'][0]['height']
        vfile.video_duration = message['outputs'][0]['duration']
        vfile.status = VideoFile.TRANSCODING_COMPLETE
        send_transcode_succeeded_mail(vfile)
        # re-export video!
        vfile.save()
        logger.info('Video changed to TRANSCODING_COMPLETE: %s' %
                    (vfile.video.key))

    elif notification_type == 'error':
        vfile.status = VideoFile.TRANSCODING_ERROR
        vfile.transcoding_result = message['outputs'][0]['statusDetail']
        logger.error('Transcoding error for video: %s' % (vfile.key))
        send_transcode_failed_mail(vfile)
    else:
        logger.error('Unknown notification_type')

    vfile.save()

    # respond with empty json
    return Response()
