from django.contrib import admin

from .models import ImagoInfoContent
from .models import ImagoInfoVideo

class ImagoInfoVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'episod_id', 'title')

admin.site.register(ImagoInfoVideo, ImagoInfoVideoAdmin)

class ImagoInfoContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'category')
    search_fields = ['name']
    list_filter = ['type', 'category']

admin.site.register(ImagoInfoContent, ImagoInfoContentAdmin)

admin.site.site_header = 'Imago TV admin'
admin.site.site_title = 'Imago TV admin site'
admin.site.index_title = None
