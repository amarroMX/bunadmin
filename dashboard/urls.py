from django.urls import path
from .views import IndexDashboardTemplateView

urlpatterns = [
    path('', IndexDashboardTemplateView.as_view(), name='dashboard'),
]