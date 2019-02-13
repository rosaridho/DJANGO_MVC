from django.shortcuts import render

from .models import Artikel

# Create your views here.
def halamanBlog(request):
    return render(request, 'blog.html')

def base_blog(request):
    artikel_obj = Artikel.objects.all()
    return render(request, 'base_blog.html', {'artikel_obj':artikel_obj})