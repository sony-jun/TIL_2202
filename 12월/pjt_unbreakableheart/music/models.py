from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.

class Song(models.Model):
    # song 제목
    song_title = models.CharField(max_length=100)
    # youtube 링크
    song_url = models.CharField(max_length=400)
    # 이미지 필드
    song_thumbnail = models.CharField(max_length=400)
    # 재생 시간
    song_runtime = models.CharField(max_length=10)