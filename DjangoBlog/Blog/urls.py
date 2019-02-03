from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('BlogList/', views.BlogList, name="BlogList"),
    path('PostCreate/', views.PostCreate, name="BlogList"),
    path('<int:post_id>/Post/', views.Post, name="BlogPost"),
]