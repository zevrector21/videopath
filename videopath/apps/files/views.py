import json

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseBadRequest

from videopath.apps.videos.models import MarkerContent, Video, VideoRevision
from videopath.apps.files.video_helper import current_file_for_video
from videopath.apps.files.image_resizer import resize_images
from videopath.apps.files.thumbnail_manager import ThumbnailManager
from videopath.apps.files.models import ImageFile, VideoFile
from videopath.apps.files.aws import verify_image_upload, get_upload_endpoint_for_image, get_upload_endpoint_for_video, verify_video_upload, start_transcoding_video
from videopath.apps.files.video_source_importers import import_url, import_custom

from rest_framework.decorators import api_view

# other stuff
@api_view(['POST', 'GET'])
def image_request_upload_ticket(request, type=None, related_id=None):

    file = ImageFile()

    # file for marker content
    if type == "marker_content":
        marker_content = get_object_or_404(MarkerContent, pk=related_id)
        if marker_content.marker.video_revision.video.user != request.user:
            return HttpResponseForbidden()

        file.image_type = file.MARKER_CONTENT
        file.save()
        marker_content.image_file.add(file)
        marker_content.save()

    # file as thumbnail
    elif type == "custom_thumbnail":
        revision = get_object_or_404(VideoRevision, pk=related_id)
        if revision.video.user != request.user:
            return HttpResponseForbidden()
        file.image_type = file.CUSTOM_THUMBNAIL
        file.save()
        revision.custom_thumbnail = file
        revision.save()

    # file as logo
    elif type == "custom_logo":
        revision = get_object_or_404(VideoRevision, pk=related_id)
        if revision.video.user != request.user:
            return HttpResponseForbidden()
        file.image_type = file.CUSTOM_LOGO
        file.save()
        revision.custom_logo = file
        revision.save()

    else:
        return HttpResponseForbidden()

    # return endpoint for upload
    endpoint = get_upload_endpoint_for_image(key=file.key)
    data = {'ticket_id': file.key, 'endpoint': endpoint,
            'marker_content_id': related_id}
    return HttpResponse(json.dumps(data), mimetype="application/json")


@api_view(['POST', 'GET'])
def image_request_upload_ticket_legacy(request, content_id=None):
    return image_request_upload_ticket(request, related_id=content_id, type="marker_content")

@api_view(['POST', 'GET'])
def image_upload_complete(request, ticket_id=None):
    ifile = get_object_or_404(ImageFile, key=ticket_id)
    file_found = verify_image_upload(ticket_id=ticket_id)
    if file_found:
        ifile.status = ImageFile.FILE_RECEIVED
        ifile.save()
    data = {
        'ticket_id': ticket_id,
        'file_found': file_found,
        'file_url': settings.IMAGE_CDN + ifile.key}
    resize_images()
    return HttpResponse(json.dumps(data), mimetype="application/json")


@api_view(['GET'])
def video_thumbs(request, video_id=None):

    video = get_object_or_404(Video, pk=video_id)
    file = current_file_for_video(video)
    if video.user != request.user or file == None or file.status != VideoFile.TRANSCODING_COMPLETE:
        return HttpResponseForbidden()

    manager = ThumbnailManager()
    available = manager.available_thumbs_for_video(video)

    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        post = json.loads(request.body)
        manager.set_thumbnail_index_for_video(video, post["index"])

    current = manager.current_thumbnail_index_for_video(video)
    data = {'index': current, 'available': available}

    return HttpResponse(json.dumps(data), mimetype="application/json")


@api_view(['POST'])
def delete_custom_thumb(request, video_id=None):
    # only allow request if video is found and user is owner
    video_revision = get_object_or_404(VideoRevision, pk=video_id)
    if video_revision.video.user != request.user:
        return HttpResponseForbidden()
    video_revision.custom_thumbnail = None
    video_revision.save()
    return HttpResponse()


@api_view(['POST', 'GET'])
def video_request_upload_ticket(request, video_id=None):

    # only allow request if video is found and user is owner
    video = get_object_or_404(Video, pk=video_id)
    if video.user != request.user:
        return HttpResponseForbidden()

    file = VideoFile()
    video.file.add(file)
    file.save()

    endpoint = get_upload_endpoint_for_video(key=file.key)
    data = {'ticket_id': file.key, 'endpoint': endpoint, 'video_id': video.id}

    # Indent the json if we are in debug mode
    return HttpResponse(json.dumps(data), mimetype="application/json")



@api_view(['POST', 'GET'])
def video_upload_complete(request, ticket_id=None):

    vfile = get_object_or_404(VideoFile, key=ticket_id)

    file_found = verify_video_upload(ticket_id=ticket_id)
    jobStarted = 0
    if file_found:
        vfile.status = VideoFile.FILE_RECEIVED
        vfile.save()
        job = start_transcoding_video(vfile)

        # save data in file
        if job:
            jobStarted = 1
            vfile.transcoding_job_id = job
            vfile.state = VideoFile.TRANSCODE_SUBMITTED
            vfile.save()
        else:
            vfile.state = VideoFile.TRANSCODING_ERROR

    data = {'ticket_id': ticket_id,
            'file_found': file_found, 'job_started': jobStarted}
    return HttpResponse(json.dumps(data), mimetype="application/json")



@api_view(['POST', 'GET'])
def import_source(request, key=None):
    video = get_object_or_404(Video, pk=key)
    if video.user != request.user:
        return HttpResponseForbidden()
    post = json.loads(request.body)

    if "url" in post:
        success, message = import_url(video, post["url"])
        if success:
            return HttpResponse(json.dumps({}))
        else:
            result = json.dumps({"error": message})
            return HttpResponseBadRequest(result)
    else:
        success, message = import_custom(video, post)
        if success:
            return HttpResponse(json.dumps({}))
        else:
            result = json.dumps({"error": message})
            return HttpResponseBadRequest(result)

    
