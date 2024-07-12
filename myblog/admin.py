from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter=['Date','Author']
    list_display=['Title','Token','Slug','Content','Image','Date','Author']
    prepopulated_fields={"Slug":('Title',)}

admin.site.register(Post,PostAdmin)