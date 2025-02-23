from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView
from .forms import ContentForm
from django.urls import reverse_lazy
from .models import Article, Favorite
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class ArticleTopView(TemplateView):
    template_name = 'articles/articles_top.html'


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

# @csrf_exempt
# def upload_image(request):
#     if request.method == 'POST' and request.FILES['header_img_url']:
#         file = request.FILES['header_img_url']
#         file_name = default_storage.save(f'header_img/{file.name}', file)
#         file_url = default_storage.url(file_name)
#         return JsonResponse({'file_url': file_url})

#     return JsonResponse({'error': 'Invalid request'}, status=400)
