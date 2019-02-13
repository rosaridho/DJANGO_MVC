from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base_blog, name='blog'),
    path('blog_new', views.input_blog, name='input_blog'),
    path('idpost', views.idpost, name='idpost'),
]

    