from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Menteebase

# Create your views here.
def base_mentee(request):
    mentee_obj = Menteebase.objects.all()
    return render(request, 'base_mentee.html', {'mentee_obj':mentee_obj})

def input_mentee(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('input_mentee')
    else:
        form = PostForm()
    
    return render(request, 'mentee_new.html', {'form':form})