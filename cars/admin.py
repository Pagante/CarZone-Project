from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def Thumbnail(self, object):
        return format_html('<img src="{}" style="border-radius:50%" width="40" />'.format(object.car_photo.url))

    list_display = ('id','Thumbnail','car_title','city','color','model','price','condition','fuel_type','is_features',)
    list_display_links = ('id','car_title','Thumbnail','city')
    list_editable = ('is_features',)
    search_fields = ('id','car_title','model','city','body_style')
    list_filter = ('city','model','body_style','year','fuel_type','price')


admin.site.register(Car, CarAdmin)
