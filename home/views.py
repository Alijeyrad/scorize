from django.shortcuts import render

# Create your views here.


def universities(request):
    return render(request, 'home/universities.html')