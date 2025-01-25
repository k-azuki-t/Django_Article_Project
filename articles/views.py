from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import ContentForm
from django.urls import reverse_lazy
from .models import Article


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