from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Commentary, Post


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_time")
    list_filter = ("user", "post", "created_time")
    search_fields = ("user", "post", "created_time")
    ordering = ("-created_time",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_time")
    list_filter = ("owner", "created_time")
    search_fields = ("title", "owner", "created_time")
    ordering = ("-created_time",)

admin.site.unregister(Group)