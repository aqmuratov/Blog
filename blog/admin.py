from django.contrib import admin
from . import models

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','image','created','updated']
    list_display_links=['title','id']

admin.site.register(models.Blog,BlogAdmin)