from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import ContentForm
from django.urls import reverse_lazy
from .models import Article
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

# Create your views here.

class ArticleTopView(TemplateView):
    template_name = 'articles/articles_top.html'

class ArticleEditView(CreateView):
    model = Article
    template_name = 'articles/articles_edit.html'
    form_class = ContentForm
    success_url = reverse_lazy('articles:top')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        # フォームの初期化時に author を設定
        form.instance.author = self.request.user
        return form
    

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES['header_img_url']:
        file = request.FILES['header_img_url']
        file_name = default_storage.save(f'header_img/{file.name}', file)
        file_url = default_storage.url(file_name)
        return JsonResponse({'file_url': file_url})

    return JsonResponse({'error': 'Invalid request'}, status=400)
