from django.views.generic import TemplateView, View

class IndexDashboardTemplateView(TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self,*args ,**kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SetLanguageView(View):
    http_method_names = ['GET']

    def get(self, request, language = 'english'):
        language = language.lower()
        print(language)


