from django.urls import path, include
from .views import *

app_name = 'articles'

urlpatterns = [
    path('', ArticleTopView.as_view(), name='top'),
    path('edit/', ArticleEditView.as_view(), name='edit'),
]