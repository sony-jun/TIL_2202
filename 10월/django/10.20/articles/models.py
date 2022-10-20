from contextlib import nullcontext
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models
from imagekit.processors import Thumbnail
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[Thumbnail(300, 400)],
        format="JPEG",
        options={"quality": 80},
    )
    thumbnail = ProcessedImageField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
