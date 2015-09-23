from django.contrib import admin

from videopath.apps.files.models import VideoFile, ImageFile, VideoSource, VideoSourceNew

class VideoFileAdmin(admin.ModelAdmin):
	list_display = ('key', 'created', 'status', 'transcoding_job_id',
	                'video_width', 'video_height', 'video_duration')
	raw_id_fields = ['video',]
	autocomplete_lookup_fields = {
	    'fk': ['video',],
	}
admin.site.register(VideoFile, VideoFileAdmin)


class ImageFileAdmin(admin.ModelAdmin):
    list_display = ('key', 'created', 'status')
admin.site.register(ImageFile, ImageFileAdmin)


class VideoSourceAdmin(admin.ModelAdmin):
	list_display = ('service', 'title', 'service_identifier', 'status', 'created')
	search_fields = ['video__key', 'service_identifier', 'video__user__username', 'service']
	raw_id_fields = ['video',]
	autocomplete_lookup_fields = {
	    'fk': ['video',],
	}
admin.site.register(VideoSource, VideoSourceAdmin)


class VideoSourceNewAdmin(admin.ModelAdmin):
	list_display = ('service', 'description', 'service_identifier', 'status', 'created')
admin.site.register(VideoSourceNew, VideoSourceNewAdmin)
