from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import ReleaseNote

# Create your views here.

class AboutKurageView(TemplateView):
    template_name = 'about/about_kurage.html'

class AboutThisSiteView(ListView):
    template_name = 'about/about_this_site.html'
    model = ReleaseNote
    context_object_name = 'release_notes'

class AboutPrivacyPolicyView(TemplateView):
    template_name = 'about/about_privacy_policy.html'

class AboutTermsOfUseView(TemplateView):
    template_name = 'about/about_terms_of_use.html'