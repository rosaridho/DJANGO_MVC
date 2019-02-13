from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.base_mentee, name='mentee'),
    path('mentee_new', views.input_mentee, name='input_mentee'),
]