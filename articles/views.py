from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from .forms import ContentForm
from django.urls import reverse_lazy
from .models import Article, Favorite
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q


# Create your views here.

class ArticleEditView(CreateView):
    model = Article
    template_name = 'articles/articles_edit.html'
    form_class = ContentForm
    success_url = reverse_lazy('articles:top')

    # フォームの初期化時に author を設定
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        # フォームの初期化時に author を設定
        form.instance.author = self.request.user
        return form
    

class ArticleDetailView(DetailView):
    model=Article
    template_name = 'articles/articles_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = self.request.user
            article = self.get_object()  # 表示対象の記事
            # お気に入り登録されているかをチェック
            is_favorited = Favorite.objects.filter(user=user, article=article).exists()
            # コンテキストに追加
            context["is_favorited"] = is_favorited
        else:
            context["is_favorited"] = False
        return context


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/articles_list.html'
    ordering = ['-created_at']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Article._meta.get_field('category').choices

        # # 1週間以内に作成された記事を取得
        # one_week_ago = timezone.now() - timedelta(days=7)
        # context['articles_ordered_by_viewed_count'] = Article.objects.filter(created_at__gte=one_week_ago).order_by('-viewed_count')[:5]

        # # お気に入り記事を取得
        # if self.request.user.is_authenticated:
        #     user = self.request.user
        #     favorited_article = Favorite.objects.filter(user=user).values('article_id')
        #     context["favorited_article"] = Article.objects.filter(article_id__in=favorited_article)

        return context
    
    # 検索機能
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-article_id')
        user = self.request.user
        query = self.request.GET.get('q')  # クエリパラメータから検索ワードを取得
        category = self.request.GET.get('category')  # クエリパラメータからカテゴリを取得
        favorite = self.request.GET.get('favorite')  # クエリパラメータからお気に入り記事を取得
        favorited_article = Favorite.objects.filter(user=user).values('article_id')

        # 検索ワードまたはカテゴリが指定されている場合、フィルタリング
        if query or category or favorite:
            queryset = queryset.filter(
                Q(content__icontains=query) &  # content に部分一致するもの
                Q(category__icontains=category) &  # category に部分一致するもの
                Q(article_id__in=favorited_article)  # お気に入り記事のみ
            )

        return queryset

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
        article.viewed_count += 1
        article.save()
        return HttpResponse(status=200)
    
    return JsonResponse({'redirect_url': '/'}, status=400)
