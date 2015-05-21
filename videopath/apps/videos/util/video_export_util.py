from videopath.apps.common.services import service_provider

from django.template import Context
from django.template.loader import get_template
from django.conf import settings

from rest_framework.renderers import JSONRenderer

from videopath.apps.videos.models import Video
from videopath.apps.videos.serializers import VideoRevisionDetailSerializer
from videopath.apps.files.util import thumbnails_util

s3_service = service_provider.get_service("s3")

#
# export a video to s3
#
def export_video(video, verbose=False):

    # 
    if video.current_revision == None or video.archived:
        return

    if verbose:
        print "exporting " + video.key

    s = _render_template(video)
    key_id = _key_for_video(video)

    # save to s3
    s3_service.upload(s, settings.AWS_PLAYER_BUCKET, key_id, content_type="text/html", cache_control = "public, max-age=600", public=True)

#
# export list of videos
#
def export_videos(videos, verbose = False):
    for video in videos:
        export_video(video, verbose)

#
# export all videos of a user
#
def export_user_videos(user):
    videos = Video.objects.filter(user=user)
    export_videos(videos)

#
# re-export all videos in the system
#
def export_all_videos(verbose=False):
    videos = Video.objects.all()
    for v in videos:
        export_video(v, verbose)

#
# delete an exported video from s3
#
def delete_export(video):
    # delete from s3
    s3_service.delete(settings.AWS_PLAYER_BUCKET, _key_for_video(video))

#
# Render an html page template for a video object
#
def _render_template(video):
    vrs = VideoRevisionDetailSerializer(video.current_revision)
    
    serialized_data = JSONRenderer().render(vrs.data)

    # get thumbnail url 
    thumb_urls = thumbnails_util.thumbnails_for_revision(video.current_revision)
    description = video.current_revision.description if video.current_revision.description and video.current_revision.description.strip() else "Watch this interactive video"

    # render template
    t = get_template('player/' + video.player_version + '/t.html')
    c = Context({
        'src_url': settings.PLAYER_SRC + video.player_version + "/",
        'video_data': serialized_data,
        'video_url': settings.PLAYER_LOCATION + video.key + "/",
        'thumb_urls': thumb_urls,
        'title': video.current_revision.title + " - Videopath",
        'description': description,
        'markers': video.current_revision.markers
    })
    return t.render(c)

#
# File key for video
#
def _key_for_video(video):
    name = video.key
    key_id = name + "/index.html"
    return key_id


