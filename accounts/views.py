from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import *
from .models import ServiceUser
from articles.models import Article, Favorite

# Create your views here.
class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = self.request.user
            favorited_article = Favorite.objects.filter(user=user).values('article_id')
            new_favorite_articles = Article.objects.filter(article_id__in=favorited_article).order_by('-created_at')[:5]
            context['new_favorite_articles'] = new_favorite_articles
        return context



# アカウント登録ビュー
class RegistrationView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/registration.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login')
    success_message = "アカウント登録が完了しました！"

    def form_invalid(self, form):
        # エラーをテンプレートに渡す
        return render(self.request, self.template_name, {'form': form})


# ログインビュー
class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    form_class = CustomAuthenticationForm
    success_message = 'ログインしました！'


# ログアウトビュー
class CustomLogutView(LogoutView):
    template_name = 'accounts/profile.html'

    def post(self, request, *args, **kwargs):
        messages.success(request, "ログアウトしました!")
        return super().post(request, *args, **kwargs)



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
class CustomPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    model = ServiceUser
    template_name = 'accounts/password_change.html'
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('accounts:profile')
    success_message = 'パスワード変更が完了しました！'

    def get_object(self):
        return self.request.user
    

class CustomDeleteView(LoginRequiredMixin, DeleteView):
    model = ServiceUser
    template_name = 'accounts/withdraw.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self):
        return self.request.user
    
    def post(self, request, *args, **kwargs):
        messages.success(request, "退会処理が完了しました。<br>またのご利用お待ちしています!")
        return super().post(request, *args, **kwargs)