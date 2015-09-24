from rest_framework import serializers

from videopath.apps.videos.models import Video, Marker, MarkerContent, VideoRevision, PlayerAppearance, Source
from videopath.apps.files.util.files_util import file_url_for_markercontent
from videopath.apps.files.util import thumbnails_util
from videopath.apps.videos.util import appearance_util


#
# Source
#
class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Source
        read_only_fields = ()



#
# Video
#
class VideoSerializer(serializers.ModelSerializer):

    revision_info = serializers.SerializerMethodField()

    thumbnails = serializers.SerializerMethodField()

    url = serializers.HyperlinkedIdentityField(view_name='video-detail')

    source = SourceSerializer(required=False, source="draft.source", read_only=True)

    def get_thumbnails(self, video):
        revision = video.draft
        return thumbnails_util.thumbnails_for_revision(revision)

    # also provide some info about the most recent revision for overviews
    def get_revision_info(self, video):
        revision = video.draft
        if revision:
            return {
                "title": revision.title,
                "draft_saved": video.draft.modified if video.draft_id != None else 0,
                "marker_count": revision.markers.count()
            }
        else:
            return {}

    def get_queryset(self):
        return Video.objects.filter(user=self.request.user)


    class Meta:
        model = Video
        fields = ('id', 'thumbnails', 'key', 'published',
                  'created', 'draft', 'current_revision', 'total_plays', 'total_views', 'revision_info', 'url', 'source')
        read_only_fields = ('user', 'draft', 'current_revision', 'archived', 'url', 'total_plays', 'total_views', 'key', 'published')

#
# Marker
#
class MarkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marker
        order_by = '-time'
        fields = ('id', 'key', 'title', 'time', 'video_revision',
                  'overlay_height', 'overlay_width')
        read_only_fields = ('overlay_height', 'overlay_width')

#
# Marker Content
#
class MarkerContentSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, content):
        return file_url_for_markercontent(content)

    class Meta:
        model = MarkerContent
        fields = ('id', 'type', 'marker', 'ordinal', 'text',
                  'data', 'title', 'url', 'image_url', 'key')

#
# Marker Content Nested
#
class NestedContentsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, content):
        return file_url_for_markercontent(content)

    class Meta:
        model = MarkerContent
        fields = ('type', 'text', 'ordinal', 'data', 'title',
                  'image_url', 'url', 'id', 'marker', 'key')

#
# Marker Nested
#
class NestedMarkerSerializer(MarkerSerializer):
    contents = NestedContentsSerializer(read_only=True, many=True)

    class Meta:
        model = Marker
        order_by = '-time'
        fields = ('id', 'key', 'title', 'time', 'video_revision',
                  'contents', 'overlay_height', 'overlay_width')
        read_only_fields = ('overlay_height', 'overlay_width')



#
# Video revision serializer
#
revision_fields = (
    'key',
    'video',
    'id',
    'title',
    'description',
    'ui_color_1',
    'ui_color_2',
    'ui_fit_video',
    'endscreen_url',
    'endscreen_title',
    'endscreen_subtitle',
    'endscreen_background_color',
    'endscreen_button_title',
    'endscreen_button_color',
    'endscreen_button_target',
    'ui_disable_share_buttons',
    'ui_equal_marker_lengths',
    'ui_icon',
    'custom_tracking_code',
    'iphone_images',
    'continuous_playback',
    'password',
    'tracking_pixel_start',
    'tracking_pixel_q1',
    'tracking_pixel_q2',
    'tracking_pixel_q3',
    'tracking_pixel_end'
)

revision_detail_fields = (
    'markers',
    'thumbnails',
    'source'
) + revision_fields

#
# Appearance
#
class PlayerAppearanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerAppearance
        exclude = ('user', 'description', 'id')

#
# Revision
#
class VideoRevisionSerializer(serializers.ModelSerializer):

    key = serializers.SerializerMethodField()
    ui_icon = serializers.SerializerMethodField()

    # some helper functions
    def get_key(self, video_revision):
        return video_revision.video.key

    def get_thumbnails(self, video_revision):
        return thumbnails_util.thumbnails_for_revision(video_revision)

    def get_ui_icon(self, video_revision):
        icon_base_url = "//images.videopath.com/icon/"
        if video_revision.ui_icon:
            return icon_base_url + video_revision.ui_icon
        return icon_base_url + "default.png"

    class Meta:
        model = VideoRevision
        fields = revision_fields
        read_only_fields = ('id', 'video')

    #
    # dynamically add extra info
    #
    def to_representation(self, instance):
        ret = super(VideoRevisionSerializer, self).to_representation(instance)

        # inject appearance
        appearance = appearance_util.appearance_for_revision(instance)
        for key, value in appearance.iteritems():
            if value != None and value != "":
                ret[key] = value

        return ret




#
# Revision with detailed info
#
class VideoRevisionDetailSerializer(VideoRevisionSerializer):

    # nested serializers
    markers = NestedMarkerSerializer(read_only=True, many=True)

    thumbnails = serializers.SerializerMethodField()
    source = SourceSerializer(required=False, read_only=True)
        

    class Meta:
        model = VideoRevision
        fields = revision_detail_fields
