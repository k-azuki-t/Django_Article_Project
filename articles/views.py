from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .forms import ContentForm
from django.urls import reverse_lazy
from .models import Article, Favorite, ArticleCategory
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
# from dateutil.relativedelta import relativedelta
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import pytz
from dateutil.relativedelta import relativedelta


# Create your views here.

class ArticleEditView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    template_name = 'articles/articles_edit.html'
    form_class = ContentForm
    success_url = reverse_lazy('articles:top')

    def test_func(self):
        user = self.request.user
        return user.is_creator

    def handle_no_permission(self):
        return redirect('articles:top')

    # フォームの初期化時に author を設定
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.instance.author = self.request.user
        return form
    

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'articles/articles_update.html'
    form_class = ContentForm
    success_url = reverse_lazy('articles:top')

    def test_func(self):
        user = self.request.user
        article = self.get_object()
        is_author_of_this_article = user == article.author

        return is_author_of_this_article

    def handle_no_permission(self):
        return redirect('articles:top')


class ArticleDetailView(DetailView):
    model=Article
    template_name = 'articles/articles_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = self.request.user
            article = self.get_object()  # 表示対象の記事
            is_favorited = Favorite.objects.filter(user=user, article=article).exists()
            is_author_of_this_article = user == article.author

            context["is_favorited"] = is_favorited
            context["is_author_of_this_article"] = is_author_of_this_article
        else:
            context["is_favorited"] = False
        return context


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/articles_list.html'
    ordering = ['-created_at']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ArticleCategory.objects.all()

        return context
    
    # 検索機能
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-article_id')
        user = self.request.user
        query = self.request.GET.get('q')  # クエリパラメータから検索ワードを取得
        category = self.request.GET.get('category')  # クエリパラメータからカテゴリを取得
        favorite = self.request.GET.get('favorite')
        created_in = self.request.GET.get('created_in')
        view_count_sort = self.request.GET.get('view_count_sort')
        page = self.request.GET.get('page', '1')

        # WHERE句追加
        if query:
            queryset = queryset.filter(
                Q(content__icontains=query) |
                Q(title__icontains=query)
            )
        if category:
            queryset = queryset.filter(category=category)
        if favorite and user.user_id != None:
            favorited_article = Favorite.objects.filter(user=user).values('article_id')
            if favorite == 'true':
                queryset = queryset.filter(article_id__in=favorited_article)
            elif favorite == 'false':
                queryset = queryset.exclude(article_id__in=favorited_article)
        if created_in:
            search_from = datetime.strptime(created_in, "%Y-%m").replace(day=1)
            search_from = timezone.make_aware(search_from, pytz.UTC)
            search_to = search_from + relativedelta(months=1)
            queryset = queryset.filter(created_at__gte=search_from, created_at__lt=search_to)
        if view_count_sort:
            if view_count_sort == 'asc':
                queryset = queryset.order_by('viewed_count__viewed_count')
            elif view_count_sort == 'desc':
                print('desc')
                queryset = queryset.order_by('-viewed_count__viewed_count')

        queryset = Paginator(queryset, 10)
        display_articles = queryset.page(int(page))

        return display_articles


# お気に入り登録用API
def registerFavorite(request, article_id):
    if not request.user.is_authenticated:
        return JsonResponse({'redirect_url': '/accounts/profile/'}, status=401)

    if request.method == 'POST':
        user = request.user
        article = Article.objects.get(article_id=article_id)
        is_favorited = Favorite.objects.filter(user=user, article=article).exists()
        
        if is_favorited:
            # お気に入り登録解除
            Favorite.objects.filter(user=user, article=article).delete()
            return JsonResponse({'is_favorited': False})
        else:
            # お気に入り登録
            Favorite.objects.create(user=user, article=article)
            return JsonResponse({'is_favorited': True})
        
    return JsonResponse({'redirect_url': '/'}, status=400)


# 記事のビュー回数を増やすAPI
def addViewedCount(request, article_id):
    if request.method == 'POST':
        article = Article.objects.get(article_id=article_id)
        article.viewed_count.viewed_count += 1
        article.viewed_count.save()
        return HttpResponse(status=200)
    
    return JsonResponse({'redirect_url': '/'}, status=400)
