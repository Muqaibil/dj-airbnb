from django.urls import path
from . import views

app_name = 'settings'


urlpatterns = [
    path('', views.home , name='home'),
    path('search/', views.home_search, name='home_search'),
    path('<str:category_name>/', views.filter_by_category, name='filter_by_category'),

]
