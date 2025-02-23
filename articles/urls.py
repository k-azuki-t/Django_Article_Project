from django.urls import path, include
from .views import *

app_name = 'articles'

urlpatterns = [
    path('', ArticleTopView.as_view(), name='top'),
    path('edit/', ArticleEditView.as_view(), name='edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('<int:article_id>/favorite/', registerFavorite, name='favorite'),
    path('<int:article_id>/addViewedCount/', addViewedCount, name='add_viewed_count'),
]