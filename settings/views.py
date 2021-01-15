from django.shortcuts import render
from settings.models import Info
from . import views
from property.models import Place, Room, Category
from blog.models import Post
from django.db.models import Q, Count
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


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

def contact(request):
    info = Info.objects.last()
    if request.method == 'POST':
        name = request.POST['name'] #getting the value from html form  and assign the value of the field 'name' to a variable
        email = request.POST['email'] #getting the value from html form  and assign the value of the field 'email' to a variable
        subject = request.POST['subject']#getting the value from html form  and assign the value of the field 'subject' to a variable
        message = request.POST['message']#getting the value from html form  and assign the value of the field 'message' to a variable
        #this method is to have a NAME html attribute in order to call the value of the field frmo django view  

        send_mail(
            subject,
            f'Message from: {name} \n Email {email} \n Message: {message}',
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )#this django email sending from documentation and using F string to format the message

    return render(request,'settings/contact.html',{'info':info})



