from django.shortcuts import render
from .models import University

# Create your views here.


def universities(request):
    universities = University.objects.all()
    context = {
        'universities': universities,
    }

    return render(request, 'home/universities.html', context)

def university(request, id):
    university = University.objects.get(id=id)
    context = {
        'uni': university,
    }

    return render(request, 'home/university.html', context)