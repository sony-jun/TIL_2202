from django.db import models
from imagekit.models import ProcessedImageField
from django.core.validators import MinValueValidator, MaxValueValidator
from imagekit.processors import ResizeToFill
from django.conf import settings
import re
from music.models import Song
from django.forms import ValidationError


from django.db.models.functions import Replace
from django.db.models import Value


with open("badwords.txt", encoding="UTF8") as file:
    CENSORED_WORDS = file.read().splitlines()


def validate_text(text):
    words = set(re.sub("[^\w]", " ", text).split())
    for censored in words:
        if censored in CENSORED_WORDS:
            raise ValidationError(f"{censored}은(는) 쓰지 말아주세요!!")


# Create your models here.
class Articles(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(validators=[validate_text])
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    picture = ProcessedImageField(
        null=True,
        upload_to="images/",
        blank=True,
        format="JPEG",
        options={"quality": 90},
    )
    disclosure = models.BooleanField(default=False)
    # True가 공개, False가 비공개
    felling_choices = (
        ("😃", "😃"),
        ("😄", "😄"),
        ("🤣", "🤣"),
        ("😍", "😍"),
        ("🥴", "🥴"),
        ("🤪", "🤪"),
        ("😐", "😐"),
        ("🙄", "🙄"),
        ("😔", "😔"),
        ("😪", "😪"),
        ("😦", "😦"),
        ("😰", "😰"),
        ("😭", "😭"),
        ("😱", "😱"),
        ("😣", "😣"),
        ("😩", "😩"),
        ("😤", "😤"),
        ("🥱", "🥱"),
        ("🥵", "🥵"),
        ("🥶", "🥶"),
    )
    feelings = models.CharField(max_length=10, choices=felling_choices)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True, blank=True)
    music_start = models.IntegerField(default=0)
    


class Comment(models.Model):
    content = models.CharField(validators=[validate_text], max_length=160)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)  # 대댓글

class ArticlesDeclaration(models.Model):
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles_reporter")
    reported = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles_writer")
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    
    class Meta:
        constraints = [
        models.UniqueConstraint(
            fields=["reporter", "articles"], name="only_one_report1"
        )
    ]

class CommentDeclaration(models.Model):
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comment_reporter")
    reported = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_writer')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    
    class Meta:
        constraints = [
        models.UniqueConstraint(
            fields=["reporter", "comment"], name="only_one_report2"
        )
    ]
    
class Sympathy(models.Model):
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    feeling = models.IntegerField(default=0)
    # 1 : 좋아요
    # 2 : 슬퍼요
    # 3 : 화나요
    # 4 : 웃겨요
    