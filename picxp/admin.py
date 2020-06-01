from django.contrib import admin
from .models import Author, tags, Picture

# Register your models here.


class PictureAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
    
admin.site.register(Author)
admin.site.register(Picture,PictureAdmin)
admin.site.register(tags)
