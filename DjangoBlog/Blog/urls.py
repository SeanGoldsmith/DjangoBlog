from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 


from . import views

urlpatterns = [
    path('', views.BlogList, name="BlogList",),
    path('PostCreate/', views.PostCreate, name="PostCreate"),
    path('<int:post_id>/Post/', views.Post, name="BlogPost"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

