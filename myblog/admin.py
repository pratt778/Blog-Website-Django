from django.contrib import admin
from .models import Post,Comments
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter=['Date','Author']
    list_display=['Title','Token','Slug','Image','Date','Author']
    prepopulated_fields={"Slug":('Title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display=['text','user','post']

admin.site.register(Comments,CommentAdmin)
admin.site.register(Post,PostAdmin)