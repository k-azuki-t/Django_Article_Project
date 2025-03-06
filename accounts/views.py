from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from .forms import *
from .models import ServiceUser

# Create your views here.
class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'


# アカウント登録ビュー
class RegistrationView(CreateView):
    template_name = 'accounts/registration.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login')
    success_message = "アカウント登録が完了しました！"

    def form_invalid(self, form):
        # エラーをテンプレートに渡す
        return render(self.request, self.template_name, {'form': form})


# ログインビュー
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'


# ログアウトビュー
class CustomLogutView(LogoutView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = 'ログアウトしました。'
        return context


# ユーザ情報変更ビュー
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


# パスワード変更ビュー
class CustomPasswordChangeView(PasswordChangeView):
    model = ServiceUser
    template_name = 'accounts/password_change.html'
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('accounts:profile')
    success_message = 'パスワード変更が完了しました！'

    def get_object(self):
        return self.request.user
    
    # def get_form_kwargs(self):
    #     """フォームに user を渡す"""
    #     kwargs = super().get_form_kwargs()
    #     kwargs['user'] = self.request.user  # user をフォームに追加
    #     return kwargs

    # def get_initial(self):
    #     initial = super().get_initial()
    #     initial['password'] = self.request.user.password
    #     return initial

@method_decorator(login_required, name="dispatch")
class CustomDeleteView(DeleteView):
    model = ServiceUser
    template_name = 'accounts/withdraw.html'
    success_url = reverse_lazy('accounts:profile')
    success_message = '退会処理が完了しました。またのご利用お待ちしています。'

    def get_object(self):
        return self.request.user