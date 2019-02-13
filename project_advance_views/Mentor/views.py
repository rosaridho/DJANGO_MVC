from django.shortcuts import render

from .models import Mentorbase

# Create your views here.
def halamanMentor(request):
    return render(request, 'mentor.html')

def base_mentor(request):
    mentor_obj = Mentorbase.objects.all()
    return render(request, 'base_mentor.html', {'mentor_obj':mentor_obj})