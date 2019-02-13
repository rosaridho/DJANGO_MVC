from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.halamanMentee, name='mentee'),
    path('basementee', views.base_mentee, name='base_mentee')
]
