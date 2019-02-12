from django.shortcuts import render

# Create your views here.
def halamanBlog(request):
    return render(request, 'blog.html')