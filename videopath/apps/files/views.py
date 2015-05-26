import json

from django.conf import settings
from django.shortcuts import get_object_or_404

from videopath.apps.videos.models import MarkerContent, Video, VideoRevision
from videopath.apps.files.util.files_util import current_file_for_video
from videopath.apps.files.util import thumbnails_util
from videopath.apps.files.models import ImageFile, VideoFile, VideoSource
from videopath.apps.files.util.aws_util import get_upload_endpoint, verify_upload, start_transcoding_video
from videopath.apps.common.services import service_provider

from rest_framework.decorators import api_view
from rest_framework.response import Response

#
# Handle image uploads
#
@api_view(['POST', 'GET'])
def image_request_upload_ticket(request, type=None, related_id=None):

    file = ImageFile()

    # file for marker content
    if type == "marker_content":
        marker_content = get_object_or_404(MarkerContent, pk=related_id)
        if marker_content.marker.video_revision.video.user != request.user:
            return Response(status=403)

        file.image_type = file.MARKER_CONTENT
        file.save()
        marker_content.image_file.add(file)
        marker_content.save()
    # file as thumbnail
    elif type == "custom_thumbnail":
        revision = get_object_or_404(VideoRevision, pk=related_id)
        if revision.video.user != request.user:
            return Response(status=403)
        file.image_type = file.CUSTOM_THUMBNAIL
        file.save()
        revision.custom_thumbnail = file
        revision.save()
    # unknown
    else:
        return Response(status=403)

    return Response({
        'ticket_id': file.key, 
        'endpoint': get_upload_endpoint(key=file.key),
        'marker_content_id': related_id
        })


@api_view(['POST', 'GET'])
def image_request_upload_ticket_legacy(request, content_id=None):
    return image_request_upload_ticket(request, related_id=content_id, type="marker_content")

@api_view(['POST', 'GET'])
def image_upload_complete(request, ticket_id=None):
    ifile = get_object_or_404(ImageFile, key=ticket_id)
    file_found = verify_upload(ticket_id=ticket_id)
    if file_found:
        ifile.status = ImageFile.FILE_RECEIVED
        ifile.save()
    service = service_provider.get_service("image_resize")
    service.resize_image_file(ifile)
    return Response({
        'ticket_id': ticket_id,
        'file_found': file_found,
        'file_url': settings.IMAGE_CDN + ifile.key
    })

#
# Handle thumbnails
#
@api_view(['GET'])
def video_thumbs(request, video_id=None):

    video = get_object_or_404(Video, pk=video_id)
    file = current_file_for_video(video)
    if video.user != request.user or file == None or file.status != VideoFile.TRANSCODING_COMPLETE:
        return Response(status=403)

    if request.method == 'POST':
        post = json.loads(request.body)
        thumbnails_util.set_thumbnail_index_for_video(video, post["index"])

    return Response({
        'index': thumbnails_util.current_thumbnail_index_for_video(video), 
        'available': thumbnails_util.available_thumbs_for_video(video)
    })


@api_view(['POST'])
def delete_custom_thumb(request, video_id=None):
    # only allow request if video is found and user is owner
    video_revision = get_object_or_404(VideoRevision, pk=video_id)
    if video_revision.video.user != request.user:
        return Response(status=403)
    video_revision.custom_thumbnail = None
    video_revision.save()
    return Response()


#
# Handle file uploads
#
@api_view(['POST', 'GET'])
def video_request_upload_ticket(request, video_id=None):

    # only allow request if video is found and user is owner
    video = get_object_or_404(Video, pk=video_id)
    if video.user != request.user:
        return Response(status=403)

    file = VideoFile()
    video.file.add(file)
    file.save()

    return Response({
        'ticket_id': file.key, 
        'endpoint': get_upload_endpoint(key=file.key), 
        'video_id': video.id
    })


@api_view(['POST', 'GET'])
def video_upload_complete(request, ticket_id=None):

    vfile = get_object_or_404(VideoFile, key=ticket_id)

    file_found = verify_upload(ticket_id=ticket_id)
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
            
    return Response({
        'ticket_id': ticket_id,
        'file_found': file_found, 
        'job_started': jobStarted
    })


#
# Import a video from youtube etc.
#
@api_view(['POST', 'GET'])
def import_source(request, key=None):

    # get video
    video = get_object_or_404(Video, pk=key)
    if video.user != request.user:
        return Response(status=403)

    service = service_provider.get_service("video_source_import")

    try:
        if "url" in request.data:
            source = service.import_video_from_url(request.data["url"])
        else:
            source = service.import_video_from_server(request.data)
    except Exception as e:
        return Response({"error": e.message}, 400)

    # create video source objects    
    VideoSource.objects.create(video=video, status=VideoSource.STATUS_OK, **source)

    # try to set title on draft
    try:
        video.draft.title = source["title"]
        video.draft.save()
    except:
        pass

    return Response()

    
