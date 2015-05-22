import json

from django.http import HttpResponse

from videopath.apps.files.models import VideoFile
from videopath.apps.files.util.aws_util import confirm_subscription
from videopath.apps.common.mailer import send_transcode_failed_mail, send_transcode_succeeded_mail

from django.conf import settings
logger = settings.LOGGER

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def process_notification(request, type):
    
    # load body
    try:
        post = json.loads(request.body)
    except BaseException:
        return HttpResponse() 

    # respond to aws subscription request
    if post['Type'] == 'SubscriptionConfirmation':
        if 'Token' in post and 'TopicArn' in post:
            confirm_subscription(post['TopicArn'], post['Token'])
            return HttpResponse()

    # retrieve video file
    message = json.loads(post['Message'])
    key = message['input']['key']
    state = message["state"]

    try:
        vfile = VideoFile.objects.get(key=key)
    except VideoFile.DoesNotExist:
        return HttpResponse()

    # parse status out of type
    if state == 'PROGRESSING':
        vfile.status = VideoFile.TRANSCODING_STARTED

    elif state == 'COMPLETED':
        vfile.video_width = message['outputs'][0]['width']
        vfile.video_height = message['outputs'][0]['height']
        vfile.video_duration = message['outputs'][0]['duration']
        vfile.status = VideoFile.TRANSCODING_COMPLETE
        send_transcode_succeeded_mail(vfile)

    elif state == 'ERROR':
        vfile.status = VideoFile.TRANSCODING_ERROR
        vfile.transcoding_result = message['outputs'][0]['statusDetail']
        send_transcode_failed_mail(vfile)

    vfile.save()

    # respond with empty json
    return HttpResponse()
