from rest_framework import serializers
from . models import Room, RoomReview



class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','owner', 'name','price','description','location','image','category']




class RoomReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomReview
        fields = ['room', 'rate','feedback']
