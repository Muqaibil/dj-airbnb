from . models import Post
from . serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

#creating serilizers using functions

@api_view(['GET',])
def post_list_api(request):
    all_post = Post.objects.all()
    data = PostSerializer(all_post, many=True).data
    return Response({'data': data})


@api_view(['GET',])
def post_detail_api (request, pk):
    post = Post.objects.get(id=pk)
    data = PostSerializer(post).data
    return Response({'data':data})