from django.contrib import admin
from .models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title",)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "article")


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
