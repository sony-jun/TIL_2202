from pyexpat import model
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.processors import Thumbnail
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(1280, 1024)],
        format="JPEG",
        options={"quality": 80},
    )
    image_thumbnail = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[Thumbnail(300, 300)],
        format="JPEG",
        options={"quality": 80},
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_articles"
    )



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
