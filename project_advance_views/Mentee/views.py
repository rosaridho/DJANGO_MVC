from django.shortcuts import render

from .models import Menteebase

# Create your views here.
def halamanMentee(request):
    return render(request, 'mentee.html')

def base_mentee(request):
    mentee_obj = Menteebase.objects.all()
    return render(request, 'base_mentee.html', {'mentee_obj':mentee_obj})
