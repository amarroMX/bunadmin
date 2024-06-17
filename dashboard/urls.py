from django.urls import path
from .views import IndexDashboardTemplateView, SetLanguageView

app_name='dashboard' 

urlpatterns = [
    path('', IndexDashboardTemplateView.as_view(), name='index'),
    path('set_language', SetLanguageView.as_view(), name='set_language'),
]