from django.urls import path
from . views import PostList, PostDetail
from .api_view import post_list_api

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path("<int:pk>", PostDetail.as_view(), name='post_detail'), 
    path('api/list', post_list_api, name='post_api_list'),

]