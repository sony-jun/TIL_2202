from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from contextlib import nullcontext

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    movie_name = models.CharField(max_length=30)
    grade = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_review"
    )


class Comment(models.Model):
    content = models.TextField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="review_comment",  # user가 comment를 불러올 때 쓰는 이름 원래는 comment_set인데, articles와 review가 구분이 안되기 때문에 구분하기 위해서 하나의 related_name를 사용한다.
    )
