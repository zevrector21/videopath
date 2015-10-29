
from django.contrib import admin

from .models import Integration

#
# Video
#
class IntegrationAdmin(admin.ModelAdmin):

    # fields
    list_display = ('user', 'service')
    ordering = ('-created',)
    search_fields = ['user', 'service']


admin.site.register(Integration, IntegrationAdmin)


