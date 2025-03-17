from django import forms
from .models import Article
from markdownx.fields import MarkdownxFormField
from markdownx.widgets import MarkdownxWidget
from django.contrib.auth.mixins import LoginRequiredMixin  # ログイン必須にするミックスイン
    
       
class ContentForm(forms.ModelForm, LoginRequiredMixin):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'header_img_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'article_title', 'placeholder': '記事タイトルを入力...'}),
            'content': MarkdownxWidget(attrs={'class': 'article_content', 'placeholder': '記事の内容を入力...'}),
            'category': forms.Select(attrs={'class': 'article_category'}),
            'header_img_url': forms.FileInput(attrs={'class': 'article_header_img'}),
        }
        labels = {
            'title': 'タイトル',
            'content': 'コンテンツ',
            'category': 'カテゴリ',
            'header_img_url': 'ヘッダー画像',
        }
    
    # def clean_header_img_url(self):
    #     header_img_url = self.cleaned_data.get('header_img_url')
    #     if not header_img_url:
    #         raise forms.ValidationError('ヘッダー画像をアップロードしてください。')
    #     return header_img_url

    #【kurage_check】form_validの役割
    #【kurage_check】viewのform_validメソッドは、フォームのバリデーションが成功した場合に呼び出されます。
    #【kurage_check】viewのget_formだと上手くいった
    # def form_valid(self, form):
    #     # ログイン中のユーザーを author に設定
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)