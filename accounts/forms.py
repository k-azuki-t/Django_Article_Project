from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import ServiceUser
from django.core.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = ServiceUser
        fields = ['name', 'email']  # 必要なフィールドを指定

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if ServiceUser.objects.filter(email=email).exists():
            raise ValidationError('このメールアドレスはすでに登録されています。')
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if not password1:
            raise ValidationError('確認用パスワードを入力してください。')
        if len(password1) < 8:
            raise ValidationError('パスワードは8文字以上で設定してください。')
        return password1
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        print(password1, password2)
        if not password2:
            raise ValidationError('確認用パスワードを入力してください。')
        if password1 is not None and password1 != password2:
            raise ValidationError('パスワードが一致しません。')
        return password2
    

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = ServiceUser
        fields = ['name', 'email']  # 必要なフィールドを指定
        widgets = {
        'name': forms.TextInput(),
        'email': forms.EmailInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        saved_email = ServiceUser.objects.get(user_id=self.instance.user_id).email
        if ServiceUser.objects.filter(email=email).exists() and email != saved_email:
            raise ValidationError('このメールアドレスはすでに登録されています。')
        return email


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = ServiceUser
        fields = ['password']  # 必要なフィールドを指定
        widgets = {
        'password': forms.PasswordInput(),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError('パスワードは8文字以上で設定してください。')
        return password