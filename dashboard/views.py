from django.views.generic import TemplateView, View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import translation
from bunadmin.settings import LANGUAGES_CODES




class IndexDashboardTemplateView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self,*args ,**kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SetLanguageView(View):
    http_method_names = ['post']

    def post(self, request, language = 'fr', next_to=reverse('dashboard:index')):
        if language not in LANGUAGES_CODES:
           set_language(request=request)
           return HttpResponseRedirect(redirect_to=next_to)
        
        set_language(request, language)
        return HttpResponseRedirect(redirect_to=next_to)
            
            

def set_language(request, language='fr'):
    translation.activate(language=language)
    request.session['django_language'] = language



