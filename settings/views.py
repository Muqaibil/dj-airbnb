from django.shortcuts import render
from . import views
from property.models import Place, Room, Category
from blog.models import Post
from django.db.models import Q, Count
from django.contrib.auth.models import User

# Create your views here.

def home(request):

    places = Place.objects.all().annotate(property_count=Count('room_place'))
    #annotaet is used to apply additional query to the main one retriving all objects. related name of relatioship is used
    # for counting the rooms in each place 
    category = Category.objects.all()

    users_count = User.objects.all().count()
    places_count = Place.objects.all().count()
    restaurant_count = Room.objects.filter(category__name='Restaurant').count()
    hotels_count = Room.objects.filter(category__name='Hotel').count()

    latest_posts = Post.objects.all()[:4]

    popular_hotels = Room.objects.filter(category__name='Hotel')[:5]
    popular_restaurant = Room.objects.filter(category__name='Restaurant')[:4]
    popular_shopping = Room.objects.filter(category__name='Shopping')[:4]

    return render(request, 'settings/home.html',{
        'places':places, 
        'category':category,
        'users_count':users_count,
        'places_count':places_count,
        'restaurant_count':restaurant_count,
        'hotels_count':hotels_count,
        'latest_posts':latest_posts,
        'popular_hotels':popular_hotels,
        'popular_restaurant':popular_restaurant,
        'popular_shopping':popular_shopping,


        })

def home_search(request):
    name = request.GET.get('text_query') 
    place = request.GET.get('place_query')

    search_result = Room.objects.filter(
        Q(name__icontains=name) & 
        Q(location__name__icontains=place) #we put __name__ in order to ask location field to check the relation related item in Place 
                                           #table where the name of the place is recorded the and the location from room table is linked
                                           #to that field

    )

    return render(request,'settings/home_search.html',{'search_result':search_result})

def filter_by_category(request, category_name):

    properties = Room.objects.filter(category__name=category_name)
    return render(request,'settings/home_search.html',{'search_result':properties})



