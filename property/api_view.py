from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Room, RoomReview
from . serializers import RoomSerializer, RoomReviewSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


#creating serilizers using CBV
class RoomListView(ListAPIView, CreateAPIView):
    model = Room
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = [IsAuthenticated]



class RoomDetailView(RetrieveUpdateDestroyAPIView):
    model = Room
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = [IsAuthenticated]