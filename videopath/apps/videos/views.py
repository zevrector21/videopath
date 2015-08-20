
from django.http import Http404

from django.shortcuts import get_object_or_404

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
from videopath.apps.videos.models import Video, Marker, MarkerContent, VideoRevision
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
        revision = video.get_or_create_draft()
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

    # Can see only your videos
    def get_queryset(self):
        videos = Video.objects.filter(user=self.request.user, archived=False)
        return videos.extra(order_by=['-created'])


    def perform_create(self, serializer):
        # add user
        instance = serializer.save(user=self.request.user)

        # if the demo attribute is present in the request
        # import demo video for this video
        try:
            demo = self.request.DATA.get("demo_project", None)
            if demo:
                from videopath.apps.files.models import VideoSource
                data = {'service': 'youtube', 'title': 'Videopath Demo Video', 'video_aspect': 1.7777777777777777, 'thumbnail_url': 'https://i.ytimg.com/vi/2rtGFAnyf-s/maxresdefault.jpg', 'video_duration': 46, 'service_identifier': '2rtGFAnyf-s'}
                VideoSource.objects.create(video=instance, status=VideoSource.STATUS_OK, **data)
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
