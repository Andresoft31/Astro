from django.urls import path
from . import views

from .views import astro

urlpatterns = [
    path('', views.home, name="home"),
    path('sample/', views.sample, name="sample"),
    path('astro/', views.astro, name='astro'),
    path('clip/', views.clip, name="clip"),
    path('blog/', views.blog, name="blog"),
    

    
   
]