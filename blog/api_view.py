from . models import Post
from . serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

#creating serilizers using functions

@api_view(['GET',])
@permission_classes([IsAuthenticated])
def post_list_api(request):
    all_post = Post.objects.all()
    data = PostSerializer(all_post, many=True).data
    return Response({'data': data})


@api_view(['GET',])
@permission_classes([IsAuthenticated])
def post_detail_api (request, pk):
    post = Post.objects.get(id=pk)
    data = PostSerializer(post).data
    return Response({'data':data})



@api_view(['GET',])
def post_search_api(request, query):
    posts = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query)
    )
    data = PostSerializer(posts, many=True).data
    return Response({'data': data})