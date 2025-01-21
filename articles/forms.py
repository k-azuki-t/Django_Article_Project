from django import forms
from .models import Article
from markdownx.fields import MarkdownxFormField

class ContentForm(forms.ModelForm):
    content = MarkdownxFormField()

    class Meta:
        model = Article
        fields = ['title', 'content']