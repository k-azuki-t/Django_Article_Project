from django.urls import path, include
from .views import *

app_name = 'product'

urlpatterns = [
    path('', ProductTopView.as_view(), name='top'),
]