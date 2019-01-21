from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^login/$', auth_views.login, {'template_name': 'core/login.html'}, name='login'),
]