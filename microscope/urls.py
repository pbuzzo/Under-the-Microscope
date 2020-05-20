from django.contrib import admin
from django.urls import path, include
from microapp.urls import urlpatterns as microapp_urls
from django.views.generic.base import TemplateView
from microapp import views


urlpatterns = [
    path('', views.index, name='home'),
    # path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    path('microapp/', include('microapp.urls')),
    path('microapp/', include('django.contrib.auth.urls')),
]

urlpatterns += microapp_urls
