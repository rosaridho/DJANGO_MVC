from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Mentorbase

def base_mentor(request):
    mentor_obj = Mentorbase.objects.all()
    return render(request, 'base_mentor.html', {'mentor_obj':mentor_obj})

def input_mentor(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('input_mentor')
    else:
        form = PostForm()

    return render(request, 'mentor_new.html', {'form':form})