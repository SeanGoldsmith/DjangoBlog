from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogList, name="BlogList",),
    path('PostCreate/', views.PostCreate, name="PostCreate"),
    path('<int:post_id>/Post/', views.Post, name="BlogPost"),
]