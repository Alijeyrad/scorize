from django.shortcuts import render
from .models import University
from django.core.paginator import Paginator
from django.db.models import Q, F

# Create your views here.


def universities(request):
    if request.method == 'POST':
        # this is when user is searching
        search_word = request.POST.get('search')
        
        universities = University.objects.all().filter(
            Q(name__contains=search_word)
            
            | Q(city__name__contains=search_word)
            
            | Q(city__country__name__contains=search_word)
        )

        paginator = Paginator(universities, 4) # Show 4 universities per page
        page_number = request.GET.get('page')
        # create page_obj that has the uni objects
        page_obj = paginator.get_page(page_number)
        # to have a list of numbers to create paginator in front
        number_of_pages = page_obj.paginator.num_pages
        number_of_pages_list = [x for x in range(1, number_of_pages + 1)]
        
        context = {
            'page_obj': page_obj,
            'num_pages': number_of_pages_list,
        }

        return render(request, 'home/universities.html', context)

    else:
        universities = University.objects.all()
        paginator = Paginator(universities, 4) # Show 4 universities per page
        page_number = request.GET.get('page')
        # create page_obj that has the uni objects
        page_obj = paginator.get_page(page_number)
        # to have a list of numbers to create paginator in front
        number_of_pages = page_obj.paginator.num_pages
        number_of_pages_list = [x for x in range(1, number_of_pages + 1)]
        
        context = {
            'page_obj': page_obj,
            'num_pages': number_of_pages_list,
        }

        return render(request, 'home/universities.html', context)


# single university view
def university(request, id):
    university = University.objects.get(id=id)
    context = {
        'uni': university,
    }

    return render(request, 'home/university.html', context)
