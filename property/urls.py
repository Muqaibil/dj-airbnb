from django.urls import path
from . import views
from . import api_view

app_name = 'property'

urlpatterns = [
    path('', views.RoomList.as_view(), name='property_list'),
    path('<slug:slug>', views.RoomDetail.as_view(), name='property_detail'),
    path('api/list', api_view.RoomListView.as_view(), name='api_room_list'),
    path('api/list/<int:pk>', api_view.RoomDetailView.as_view(), name='api_room_detail'),
]