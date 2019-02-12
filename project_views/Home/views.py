from django.shortcuts import render

# Create your views here.
def halamanHome(request):
    return render(request,'home.html')