from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView
# Create your views here.

class RoomList(ListView):
    model = models.Room

class RoomDetail(DetailView):
    model = models.Room