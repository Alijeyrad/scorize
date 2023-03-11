from django.shortcuts import render
from .models import University, City, Country
from django.core.paginator import Paginator
from django.db.models import Q, F
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Create your views here.

def universities(request):
    if request.method == 'POST':        
        # this is when user is searching
        search_word = request.POST.get('search')
        
        universities = University.objects.all().filter(
            Q(name__contains=search_word)
            
            | Q(city__name__contains=search_word)
            
            | Q(city__country__name__contains=search_word)
        ).order_by('-date_established')
    else:
        universities = cache.get('universities')
        if universities is None:
            universities = University.objects.all().order_by('-date_established')
            cache.set('universities', universities, 60 * 15)  # Cache for 15 minutes
    
    cities = cache.get('cities')
    if cities is None:
        cities = City.objects.all()
        cache.set('cities', cities, 60 * 15) 
    
    countries = cache.get('countries')
    if countries is None:
        countries = Country.objects.all()
        cache.set('countries', countries, 60 * 15) 

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
        'countries': countries,
        'cities': cities
    }

    return render(request, 'home/universities.html', context)


def filter_uni(request, keyword):
    if keyword != 'None':
        universities = University.objects.all().filter(
            Q(city__name__contains=keyword)
                
            | Q(city__country__name__contains=keyword)
        ).order_by('-date_established')
    else:
        universities = cache.get('universities')
        if universities is None:
            universities = University.objects.all().order_by('-date_established')
            cache.set('universities', universities, 60 * 15) 

    cities = cache.get('cities')
    if cities is None:
        cities = City.objects.all()
        cache.set('cities', cities, 60 * 15) 
    
    countries = cache.get('countries')
    if countries is None:
        countries = Country.objects.all()
        cache.set('countries', countries, 60 * 15) 

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
        'countries': countries,
        'cities': cities,
        'keyword': keyword
    }

    return render(request, 'home/universities.html', context)


# single university view
@cache_page(60 * 15)  # Cache for 15 minutes
def university(request, id):
    university = University.objects.get(id=id)
    context = {
        'uni': university,
    }

    return render(request, 'home/university.html', context)
