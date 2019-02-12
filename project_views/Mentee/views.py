from django.shortcuts import render

# Create your views here.
def halamanMentee(request):
    return render(request, 'mentee.html')
