from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import *
from .models import ServiceUser

# Create your views here.
class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'


class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login')
    success_message = "アカウント登録が完了しました！"

    def form_invalid(self, form):
        # エラーをテンプレートに渡す
        return render(self.request, self.template_name, {'form': form})


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'


class CustomLogutView(LogoutView):
    template_name = 'accounts/profile.html'


class CustomUserUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = ServiceUser
    template_name = 'accounts/profile_change.html'
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('accounts:profile')
    success_message = "アカウント情報の変更が完了しました！"

    # Generic detail view CustomUserUpdateView must be called with either an object pk or a slug in the URLconf.
    def get_object(self):
        return self.request.user
    
    def get_initial(self):
        """フォームの初期値を設定"""
        initial = super().get_initial()
        initial['name'] = self.request.user.name
        initial['email'] = self.request.user.email
        return initial


class CustomPasswordChangeView(LoginRequiredMixin, UpdateView):
    model = ServiceUser
    template_name = 'accounts/password_change.html'
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('accounts:profile')
    success_message = "パスワード変更が完了しました！"

    def get_object(self):
        return self.request.user

    def get_initial(self):
        initial = super().get_initial()
        initial['password'] = self.request.user.password
        return initial