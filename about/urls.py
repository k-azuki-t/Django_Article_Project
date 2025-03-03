from django.urls import path, include
from .views import *

app_name = 'about'

urlpatterns = [
    path('kurage/', AboutKurageView.as_view(), name='kurage'),
    path('this_site/', AboutThisSiteView.as_view(), name='this_site'),
    path('this_site/privacy_policy/', AboutPrivacyPolicyView.as_view(), name='privacy_policy'),
    path('this_site/terms_of_use/', AboutTermsOfUseView.as_view(), name='terms_of_use'),
]