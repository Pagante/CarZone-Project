from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    def Image(self, object):
        return format_html('<img src="{}" style="border-radius:50%" width="40"/>'.format(object.photo.url))
    list_display = ('id', 'Image', 'first_name','last_name','designation','created_date')
    list_display_links = ('id', 'first_name','last_name')
    search_fields = ('first_name','last_name','designation')
    list_filter = ('designation',)


admin.site.register(Team, TeamAdmin)
