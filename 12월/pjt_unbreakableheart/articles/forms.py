from django import forms
from .models import *
from django.forms import FileInput, Select


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = [
            "music_start",
            "content",
            "feelings",
            "picture",
            "disclosure",
        ]
        labels = {
            "content": "오늘의 하루",
            "picture": "이미지",
            "feelings": "감정표현",
            "music_start": "음악을 재생할 위치를 정해주세요.(초)",
            "disclosure": "공개하기",
        }
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "border border-dark rounded-15 mx-1",
                    "style": "background: transparent; border-radius:15px; border:1.5px solid rgb(51, 51, 51)!important; box-shadow:none!important;",
                    "placeholder": "당신의 오늘을 이야기해주세요.",
                }
            ),
            "picture": FileInput(
                attrs={
                    "class": "border border-dark rounded-15 mx-1",
                    "style": "background: transparent; border:1.5px solid rgb(51, 51, 51)!important; box-shadow:none!important;",
                }
            ),
            "feelings": Select(
                attrs={
                    "class": "border border-dark rounded-15 mx-1",
                    "style": "background: transparent; border:1.5px solid rgb(51, 51, 51)!important; box-shadow:none!important;",
                    "placeholder": "오늘의 기분을 말해주세요.",
                }
            ),
            "music_start": forms.NumberInput(
                attrs={
                    "class": "border border-dark rounded-15 mx-1",
                    "style": "background: transparent;border:1.5px solid rgb(51, 51, 51)!important; box-shadow:none!important;",
                }
            ),
            "disclosure": forms.CheckboxInput(
                attrs={"class": "form-check-input", "id": "flexSwitchCheckChecked"}
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]

        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 2,
                    "style": "background: transparent;",
                    "class": "border border-2 border-dark bg-white rounded-1 text-dark p-3 font-space shadow-sm scroll-none",
                }
            ),
        }

        labels = {
            "content": "",
        }


class ArticlesDeclarationForm(forms.ModelForm):
    class Meta:
        model = ArticlesDeclaration
        fields = [
            "content",
        ]
        labels = {
            "content": "신고내용",
        }


class CommentDeclarationForm(forms.ModelForm):
    class Meta:
        model = CommentDeclaration
        fields = [
            "content",
        ]
        labels = {
            "content": "신고내용",
        }
