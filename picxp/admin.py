from django.contrib import admin
from .models import location, category, Image

# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('location','category')
    
admin.site.register(location)
admin.site.register(Image,ImageAdmin)
admin.site.register(category)
