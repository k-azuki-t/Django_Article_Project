
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import ServiceUser


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        "invalid_login": _(
            "正しい%(username)sとパスワードを入力してください。 "
        ),
        "inactive": _("This account is inactive."),
    }


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = ServiceUser
        fields = ['name', 'email', 'password1', 'password2']  # 必要なフィールドを指定

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password1, password2 = self.create_password_fields()
        self.fields["password1"] = password1
        self.fields["password2"] = password2
    
    # テンプレート側でのパスワード・確認用パスワードを入力必須化
    @staticmethod
    def create_password_fields(label1=_("Password"), label2=_("Password confirmation")):
        password1 = forms.CharField(
            label=label1,
            required=True,
            strip=False,
            widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
            help_text=password_validation.password_validators_help_text_html(),
        )
        password2 = forms.CharField(
            label=label2,
            required=True,
            widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
            strip=False,
            help_text=_("Enter the same password as before, for verification."),
        )
        return password1, password2

    # メールアドレスのバリデータはUserCreationFormに存在しないため、自身で定義
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if ServiceUser.objects.filter(email=email).exists():
            raise ValidationError('このメールアドレスはすでに登録されています。')
        return email
    

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