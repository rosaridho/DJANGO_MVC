from django.shortcuts import render

# Create your views here.
def halamanAuthor(request):
    return render(request, 'author.html')