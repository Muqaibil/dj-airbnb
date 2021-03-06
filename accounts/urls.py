from django.urls import path
from .views import profile , profile_edit , signup , user_reservation, add_feedback, user_rooms


app_name = 'accounts'

urlpatterns = [
    path('signup',signup , name='signup'),
    path('profile/',profile,name='profile'),
    path('profile/reservation',user_reservation,name='user_reservation'),
    path('profile/rooms',user_rooms,name='user_rooms'),
    path('profile/reservation/<slug:slug>/review',add_feedback,name='add_feedback'),
    path('profile/edit', profile_edit , name='profile_edit')
]
