from django.shortcuts import render
from .models import University

# Create your views here.


def universities(request):
    universities = University.objects.all()
    context = {
        'universities': universities,
    }

    return render(request, 'home/universities.html', context)