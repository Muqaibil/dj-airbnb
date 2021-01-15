from django.shortcuts import redirect, render, get_object_or_404
from .models import Profile
from .forms import UserForm , ProfileForm , UserCreateForm
from django.urls import reverse
from django.contrib.auth import authenticate, login
from property.models import RoomBook, Room
from property.forms import RoomReviewForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        signup_form = UserCreateForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            # return redirect(reverse('login'))
            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse('accounts:profile'))
    
    else:
        signup_form = UserCreateForm()

    return render(request,'registration/signup.html',{'signup_form':signup_form})



def profile(request):
    profile = Profile.objects.get(user = request.user)
    return render(request,'profile/profile.html',{'profile':profile})



def profile_edit(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST , instance=request.user)
        profile_form = ProfileForm(request.POST , request.FILES , instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            my_form = profile_form.save(commit=False)
            my_form.user = request.user
            my_form.save()
            return redirect(reverse('accounts:profile'))
    
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance = profile)       

    return render(request,'profile/profile_edit.html',{
        'user_form' : user_form , 
        'profile_form' : profile_form
    })


def user_reservation(request):
    my_reservation = RoomBook.objects.filter(name=request.user)
    return render(request,'profile/my_reservation.html',{'my_reservation':my_reservation})


def user_rooms(request):
    my_rooms = Room.objects.filter(owner=request.user)
    return render(request,'profile/my_rooms.html',{'my_rooms':my_rooms})


def add_feedback(request, slug):
    room = get_object_or_404(Room, slug=slug)
    if request.method == 'POST':
        form = RoomReviewForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.room = room
            myform.author = request.user
            myform.save()

            return redirect(reverse('rooms:property_detail', kwargs={'slug': room.slug}))
        
    else:
        form = RoomReviewForm()

    return render(request, 'profile/add_review.html',{'form':form})
    











