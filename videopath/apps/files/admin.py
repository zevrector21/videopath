from django.contrib import admin

from videopath.apps.files.models import VideoFile, ImageFile, VideoSource

class VideoFileAdmin(admin.ModelAdmin):
    list_display = ('key', 'created', 'status', 'transcoding_job_id',
                    'video_width', 'video_height', 'video_duration')
    pass
admin.site.register(VideoFile, VideoFileAdmin)


class ImageFileAdmin(admin.ModelAdmin):
    list_display = ('key', 'created', 'status')
    pass
admin.site.register(ImageFile, ImageFileAdmin)


class VideoSourceAdmin(admin.ModelAdmin):
    list_display = ('service', 'title', 'service_identifier', 'status')
    pass
admin.site.register(VideoSource, VideoSourceAdmin)
