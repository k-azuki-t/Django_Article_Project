from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class AboutKurageView(TemplateView):
    template_name = 'about/about_kurage.html'

class AboutThisSiteView(TemplateView):
    template_name = 'about/about_this_site.html'

class AboutPrivacyPolicyView(TemplateView):
    template_name = 'about/about_privacy_policy.html'

class AboutTermsOfUseView(TemplateView):
    template_name = 'about/about_terms_of_use.html'