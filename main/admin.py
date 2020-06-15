from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Courses, Video, Comment

admin.site.register(Courses)

admin.site.register(Video)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)



class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass