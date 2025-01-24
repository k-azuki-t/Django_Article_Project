from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import ContentForm
from django.urls import reverse_lazy


# Create your views here.

class ArticleTopView(TemplateView):
    template_name = 'articles/articles_top.html'

class ArticleEditView(FormView):
    template_name = 'articles/articles_edit.html'
    form_class = ContentForm
    success_url = reverse_lazy('articles:top')