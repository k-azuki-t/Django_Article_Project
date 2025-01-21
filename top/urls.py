from django.urls import path, include
from .views import *

app_name = 'top'

urlpatterns = [
    path('', TopView.as_view(), name='top'),
]