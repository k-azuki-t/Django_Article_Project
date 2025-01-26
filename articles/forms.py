from django import forms
from .models import Article
from markdownx.fields import MarkdownxFormField
from django.contrib.auth.mixins import LoginRequiredMixin  # ログイン必須にするミックスイン


# class ContentForm(forms.ModelForm):
#     content = MarkdownxFormField()

#     class Meta:
#         model = Article
#         fields = ['title', 'content', 'category', 'header_img_url']

#     def clean_category(self):
#         category = self.cleaned_data['category']
#         print(category)
    
        
class ContentForm(forms.ModelForm, LoginRequiredMixin):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'header_img_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '記事のタイトルを入力してください'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '記事の内容を入力してください'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            # 'header_img_url': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'header_img_url': forms.HiddenInput(),  # Dropzone.jsが担当するためHiddenに変更
        }
        labels = {
            'title': 'タイトル',
            'content': 'コンテンツ',
            'category': 'カテゴリ',
            'header_img_url': 'ヘッダー画像',
        }

    #【kurage_check】form_validの役割
    #【kurage_check】viewのform_validメソッドは、フォームのバリデーションが成功した場合に呼び出されます。
    #【kurage_check】viewのget_formだと上手くいった
    # def form_valid(self, form):
    #     # ログイン中のユーザーを author に設定
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)