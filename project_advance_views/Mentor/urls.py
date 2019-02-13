from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base_mentor, name='mentor'),
    path('mentor_new', views.input_mentor, name='input_mentor'),
]