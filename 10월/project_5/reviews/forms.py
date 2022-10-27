from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title','content','image','image_thumbnail',]
        labels = {
            'title' : '제목',
            'content' : '내용',
            'image' : '이미지',
            'image_thumbnail' : '썸네일',
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content',]
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'cols': 40})
        }
        labels = {
        'content': '',
        }