
from django.http import Http404

from django.shortcuts import get_object_or_404

from django.db.models import Q

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, ValidationError
from rest_framework.decorators import permission_classes, renderer_classes, parser_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import MultiPartParser, FormParser


from videopath.apps.videos.util.oembed_xml_renderer import OEmbedXMLRenderer
from videopath.apps.videos.util import share_mail_util, oembed_util, icon_util
from videopath.apps.videos.permissions import MarkerPermissions, VideoPermissions, MarkerContentPermissions, VideoRevisionPermissions, AuthenticatedPermission
from videopath.apps.videos.models import Video, Marker, MarkerContent, VideoRevision, Source
from videopath.apps.videos.serializers import VideoRevisionDetailSerializer, VideoSerializer, MarkerSerializer, MarkerContentSerializer, VideoRevisionSerializer
from videopath.apps.common.services import service_provider


from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny


#
# Upload or delete icon
#
@api_view(['DELETE', 'PUT'])
@permission_classes((AllowAny,))
@parser_classes((MultiPartParser,FormParser))
def icon_view(request, rid=None):

    try:
        revision = VideoRevision.objects.get(video__user = request.user, pk=rid)
        if request.method == "PUT":
            ok, detail = icon_util.handle_uploaded_icon(revision, request.data["file"])
            if not ok:
                raise ValidationError(detail)
            return Response({},201)
        elif request.method == "DELETE":
            revision.ui_icon = None
            revision.save()
    except VideoRevision.DoesNotExist:
        raise Http404

    

#
# Upload or delete thumbnail
#
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes((AllowAny,))
@parser_classes((MultiPartParser,FormParser))
def thumbnail_view(request, rid=None):

    if request.method == "PUT":
        pass
    elif request.method == "DELETE":
        pass
    elif request.method == "GET":
        pass

    return Response({})

#
# Support for oEmbed info
#
@api_view(['GET'])
@permission_classes((AllowAny,))
@renderer_classes((JSONRenderer,OEmbedXMLRenderer,))
def oembed(request):

    result = oembed_util.parse(request.GET)

    if result == 401:
        return Response(status=401)
    elif result == 404:
        return Response(status=404)

    return Response(result)

#
# Get revision of a video
#
@api_view(['GET'])
def get_revision(request, vid=None, rev_type='published'):

    # see wether this should be the published or draft version
    published = rev_type == 'published'

    # see wether this should be the expanded view
    expanded = request.GET.get('expanded', '0')

    # load the video and the correct serializer
    video = Video.objects.get_video_or_404(vid, request.user)

    # find the correct revision
    if published and video.current_revision_id:
        revision = video.current_revision
    elif not published:
        revision = video.draft
    else:
        raise Http404

    serializer = VideoRevisionDetailSerializer(revision) if expanded else VideoRevisionSerializer(revision)
    return Response(serializer.data)


#
# Publish and unpublish a video
#
@api_view(['PUT', 'DELETE'])
def video_publish(request, vid=None):

    video = get_object_or_404(Video, pk=vid, user=request.user)

    if request.method == 'PUT':
        video.publish()
        slack = service_provider.get_service("slack")
        slack.notify("User " + request.user.email + " just published video http://player.videopath.com/" + video.key + ". ")


    if request.method == 'DELETE':
        video.unpublish()

    return Response({})

#
# Send a share email
# 
@api_view(['POST'])
def send_share_mail(request, vid=None):
    video = get_object_or_404(Video, pk=vid, user=request.user)
    success, detail = share_mail_util.send_share_mail(video, request.DATA.get("recipients", ""), request.DATA.get("message",""))

    if not success:
        raise ParseError(detail=detail)

    return Response({})

#
# View Set of Videos
#
class VideoViewSet(viewsets.ModelViewSet):
    model = Video
    serializer_class = VideoSerializer
    permission_classes = (VideoPermissions,AuthenticatedPermission)

    # Can see only your videos, filterable by q
    def get_queryset(self):
        videos = Video.objects.filter(user=self.request.user, archived=False)
        q = self.request.GET.get('q')
        if q:
            q = q.strip()
            videos = videos.filter(Q(draft__title__icontains = q) | Q(draft__description__icontains = q))
        return videos.extra(order_by=['-created'])

    def create(self, request, *args, **kwargs):
        copy_source=self.request.DATA.get("copy_source", None)
        if copy_source:
            copy_source = Video.objects.get(pk=copy_source, user=self.request.user)
            copy_source.duplicate() 
            return Response({}, status=status.HTTP_201_CREATED)
        return super(VideoViewSet, self).create(request,*args, **kwargs)

    def perform_create(self, serializer):
        # add user
        instance = serializer.save(user=self.request.user)

        # if the demo attribute is present in the request
        # import demo video for this video
        try:
            demo = self.request.DATA.get("demo_project", None)
            if demo:
                from videopath.apps.videos.models import Source
                thumb = 'https://i.ytimg.com/vi/2rtGFAnyf-s/maxresdefault.jpg'
                data = {'service': 'youtube', 'description': 'Videopath Demo Video', 'aspect': 1.7777777777777777, 'thumbnail_small': thumb, 'thumbnail_large': thumb, 'duration': 46, 'service_identifier': '2rtGFAnyf-s'}
                instance.draft.source = Source.objects.create( status=Source.STATUS_OK, **data)
                instance.draft.save()
        except:
            raise ValidationError(detail="Unknown demo project")
        

    def destroy(self, request, *args, **kwargs):
        # videos never get deleted, only archived
        obj = self.get_object()
        obj.archived = True
        obj.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

#
# Video Revisions View Set
#
class VideoRevisionViewSet(viewsets.ModelViewSet):

    model = VideoRevision
    serializer_class = VideoRevisionSerializer
    permission_classes = (VideoRevisionPermissions,AuthenticatedPermission)

    # revisions will always be created through the system
    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # revisions will always be deleted through the system
    def delete(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # Can see only your videos
    def get_queryset(self):
        return VideoRevision.objects.filter(video__user=self.request.user)

#
# Marker View Set
#
class MarkerViewSet(viewsets.ModelViewSet):
    model = Marker
    serializer_class = MarkerSerializer
    permission_classes = (MarkerPermissions,AuthenticatedPermission)

    def get_queryset(self, vid = None):
        if vid:
            return Marker.objects.filter(video_revision__video__user=self.request.user, video_revision__id=vid)
        else:
            return Marker.objects.filter(video_revision__video__user=self.request.user)

#
# Marker Content View Set
#
class MarkerContentViewSet(viewsets.ModelViewSet):
    model = MarkerContent
    serializer_class = MarkerContentSerializer
    permission_classes = (MarkerContentPermissions,AuthenticatedPermission)

    def get_queryset(self, mid = None):
        if mid:
            return MarkerContent.objects.filter(marker__video_revision__video__user=self.request.user, marker__id=mid)
        else:
            return MarkerContent.objects.filter(marker__video_revision__video__user=self.request.user)

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
    video.draft.source = Source.objects.create(status=Source.STATUS_OK, **source)
    video.draft.save()

    if "url" in request.data:
        slack = service_provider.get_service("slack")
        slack.notify("User " + request.user.email + " just imported video " + request.data["url"] + ".")

    # try to set title on draft
    try:
        if not video.draft.title or video.draft.title == "New Video":
            video.draft.title = source["description"]
        video.draft.save()
    except:
        pass

    return Response()
