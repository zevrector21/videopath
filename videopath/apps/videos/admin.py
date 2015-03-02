import humanize

from django.contrib import admin

from videopath.apps.files.models import VideoSource, VideoFile
from videopath.apps.videos.models import Video, Marker, MarkerContent, VideoRevision, PlayerAppearance

#
# Video file inline
#
class VideoFileInlineAdmin(admin.TabularInline):
    model = VideoFile

#
# Video source inline
#
class VideoSourceInlineAdmin(admin.TabularInline):
    model = VideoSource

#
# Video
#
class VideoAdmin(admin.ModelAdmin):
    list_display = ('key', 'id', 'user', 'revision_link', 'created_humanized',
                    'modified_humanized',  'draft_link', 'current_revision_link', 'archived')
    list_filter = ('user__username',)
    ordering = ('-created',)
    search_fields = ['key', 'id']
    inlines = (VideoFileInlineAdmin, VideoSourceInlineAdmin)

    def created_humanized(self, obj):
        return humanize.naturaltime(obj.created)

    def modified_humanized(self, obj):
        return humanize.naturaltime(obj.modified)

    def revision_link(self, obj):
        link = "/admin/videos/videorevision/?video__key=" + obj.key
        return "<a href = '" + link + "'>List of Revisions</a> (" + str(obj.revisions.count()) + ")"
    revision_link.allow_tags = True

    def draft_link(self, obj):
        if not obj.draft:
            return "None"
        link = "/admin/videos/videorevision/?id=" + str(obj.draft.id)
        return "<a href = '" + link + "'>Current Draft</a>"
    draft_link.allow_tags = True

    def current_revision_link(self, obj):
        if not obj.current_revision:
            return "None"
        link = "/admin/videos/videorevision/?id=" + \
            str(obj.current_revision.id)
        return "<a href = '" + link + "'>Current Revision</a>"
    current_revision_link.allow_tags = True

    def __unicode__(self):
        return "Video " + self.key

admin.site.register(Video, VideoAdmin)


#
# Marker
#
class MarkerInlineAdmin(admin.TabularInline):
    model = Marker

#
# Revision
#
class VideoRevisionAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'marker_link', 'created_humanized', 'modified_humanized')
    search_fields = ['title']
    ordering = ('-created',)
    list_filter = ('video__key', 'id')
    inlines = (MarkerInlineAdmin, )

    fieldsets = (
        ('General', {
            'fields': ('video', 'title', 'description', 'iphone_images', 'player_appearance')
        }),
        ('Appearance', {
            'fields': ('ui_color_1', 'ui_color_2')
        }),
        ('Endscreen', {
            'fields': ('endscreen_url', 'endscreen_title', 'endscreen_background_color', 'endscreen_button_title', 'endscreen_button_target', 'endscreen_button_color')
        }),
        ('Files', {
            'fields': ('custom_thumbnail', )
        })
    )

    def created_humanized(self, obj):
        return humanize.naturaltime(obj.created)

    def modified_humanized(self, obj):
        return humanize.naturaltime(obj.modified)

    def marker_link(self, obj):
        link = "/admin/videos/marker/?video_revision__id=" + str(obj.id)
        return "<a href = '" + link + "'>List of Markers</a> (" + str(obj.markers.count()) + ")"
    marker_link.allow_tags = True

admin.site.register(VideoRevision, VideoRevisionAdmin)


#
# Marker
#
class MarkerAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'video_revision', 'content_link')
    list_filter = ('video_revision__id',)
    ordering = ('time',)

    def content_link(self, obj):
        link = "/admin/videos/markercontent/?marker__id=" + str(obj.id)
        return "<a href = '" + link + "'>List of Contents</a> (" + str(obj.contents.count()) + ")"
    content_link.allow_tags = True

admin.site.register(Marker, MarkerAdmin)


#
# Marker Content
#
class MarkerContentAdmin(admin.ModelAdmin):
    list_display = ('ordinal', 'type')
    list_filter = ('marker__id',)
    ordering = ('ordinal',)

admin.site.register(MarkerContent, MarkerContentAdmin)


#
# Appearance
#
class PlayerAppearanceAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General', {
            'fields': ('description', 'user')
        }),
        ('Colors', {
            'fields': ('ui_color_1', 'ui_color_2')
        }),
        ('Colors Advanced', {
            'classes': ('collapse',),
            'fields': (
                'ui_color_playbar_outline','ui_color_playbar_background','ui_color_playbar_progress','ui_color_playbar_buffer', 'ui_color_playbar_indicators',
                'ui_color_marker_background','ui_color_marker_outline','ui_color_marker_text',
                'ui_color_marker_highlight_background','ui_color_marker_highlight_outline','ui_color_marker_highlight_text',
                'ui_color_button_background','ui_color_button_text','ui_color_button_highlight_background','ui_color_button_highlight_text',
                'ui_color_overlay_outline',)
        }),
        ('Images', {
            'fields': ('endscreen_logo', 'icon')
        }),
        ('Fonts', {
            'fields': ('ui_font_marker', 'ui_font_overlay_titles', 'ui_font_overlay_text')
        }),
        ('Other', {
            'fields': ('language', 'sharing_disabled')
        })
    )

admin.site.register(PlayerAppearance, PlayerAppearanceAdmin)

