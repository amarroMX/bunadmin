from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('users.urls'), name='users'),
    path('admin/', admin.site.urls),
    path('dashboard', include('dashboard.urls')),
]
