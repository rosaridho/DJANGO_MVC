from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.halamanMentor, name='mentor'),
    path('basementor', views.base_mentor, name='base_mentor')
]