from django.urls import path
from . import views

app_name = 'property'

urlpatterns = [
    path('', views.RoomList.as_view()),
    path('<slug:slug>', views.RoomDetail.as_view()),
]