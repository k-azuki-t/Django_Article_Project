from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import ReleaseNote, MySkill, MyCareer, InterestedDomain, Capabilities, SkillCategory

# Create your views here.

class AboutKurageView(TemplateView):
    template_name = 'about/about_kurage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_skills'] = MySkill.objects.all()
        context['skill_categories'] = SkillCategory.objects.all()
        context['my_careers'] = MyCareer.objects.all().order_by('career_started_at')
        context['interested_domains'] = InterestedDomain.objects.all()
        context['capabilities'] = Capabilities.objects.all()
        return context

class AboutThisSiteView(ListView):
    template_name = 'about/about_this_site.html'
    model = ReleaseNote
    context_object_name = 'release_notes'

class AboutPrivacyPolicyView(TemplateView):
    template_name = 'about/about_privacy_policy.html'

class AboutTermsOfUseView(TemplateView):
    template_name = 'about/about_terms_of_use.html'