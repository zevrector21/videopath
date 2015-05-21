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

    post = request.data

    # respond to aws subscription request
    if post['Type'] == 'SubscriptionConfirmation':
        if 'Token' in post and 'TopicArn' in post:
            confirm_subscription(post['TopicArn'], post['Token'])
            return Response({"status": "subs confirmation"})

    # retrieve video file
    message = json.loads(post['Message'])
    key = message['input']['key']

    try:
        vfile = VideoFile.objects.get(key=key)
    except VideoFile.DoesNotExist:
        return Response({"status":"did not find file"})

    # parse status out of type
    if notification_type == 'progressing':
        vfile.status = VideoFile.TRANSCODING_STARTED

    elif notification_type == 'complete':
        vfile.video_width = message['outputs'][0]['width']
        vfile.video_height = message['outputs'][0]['height']
        vfile.video_duration = message['outputs'][0]['duration']
        vfile.status = VideoFile.TRANSCODING_COMPLETE
        send_transcode_succeeded_mail(vfile)

    elif notification_type == 'error':
        vfile.status = VideoFile.TRANSCODING_ERROR
        vfile.transcoding_result = message['outputs'][0]['statusDetail']
        send_transcode_failed_mail(vfile)

    else:
        logger.error('Unknown notification_type')

    vfile.save()

    # respond with empty json
    return Response({"status": "ok"})
