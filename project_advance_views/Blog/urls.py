from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base_blog, name='blog'),
    path('blog_new', views.input_blog, name='input_blog'),
    path('<int:post_id>', views.idpost_blog, name='idpost_blog'),
]