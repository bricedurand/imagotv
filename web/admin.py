from django.contrib import admin

from .models import Content
from .models import Media

class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'episode_number')

admin.site.register(Media, MediaAdmin)

class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'category')

admin.site.register(Content, ContentAdmin)

admin.site.site_header = 'Imago TV admin'
admin.site.site_title = 'Imago TV admin site'
admin.site.index_title = None
