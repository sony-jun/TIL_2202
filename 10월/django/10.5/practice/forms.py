from django import forms
from .models import Practice


class PracticeForm(forms.ModelForm):
    class Meta:
        model = Practice
        fields = ["title", "content"]
