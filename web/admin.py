from django.contrib import admin

from .models import Content
from .models import Media

class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_id', 'episode_number', 'title')

admin.site.register(Media, MediaAdmin)

class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'category')
    search_fields = ['name']
    list_filter = ['type', 'category']

admin.site.register(Content, ContentAdmin)

admin.site.site_header = 'Imago TV admin'
admin.site.site_title = 'Imago TV admin site'
admin.site.index_title = None
