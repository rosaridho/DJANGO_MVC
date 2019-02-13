from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Artikel

# Create your views here
def base_blog(request):
    artikel_obj = Artikel.objects.all()
    return render(request, 'base_blog.html', {'artikel_obj':artikel_obj})

def input_blog(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('input_blog')
    else:
        form = PostForm()

    return render(request, 'blog_new.html', {'form':form})


def idpost(request):
    idpost_obj = Artikel.objects.all()
    return render(request, 'idpost.html', {'idpost_obj':idpost_obj})