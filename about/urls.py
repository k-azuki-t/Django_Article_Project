from django.urls import path, include
from .views import *

app_name = 'about'

urlpatterns = [
    path('kurage/', AboutKurageView.as_view(), name='kurage'),
    path('this_site/', AboutThisSiteView.as_view(), name='this_site'),
]