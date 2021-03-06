from django.shortcuts import render, redirect
from . import models
from django.views.generic import ListView, DetailView, CreateView
from django_filters.views import FilterView
from . filters import PropertyFilter
from django.views.generic.edit import FormMixin
from . forms import RoomBookForm

from django.urls import reverse

# Create your views here.

class RoomList(FilterView):
    model = models.Room
    filterset_class = PropertyFilter
    template_name = 'property/room_list.html'
    paginate_by = 4

class RoomDetail(FormMixin, DetailView):
    model = models.Room
    form_class = RoomBookForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_property"] = models.Room.objects.filter(category=self.get_object().category)
        return context


    def post (self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.room = self.object
            myform.save()

        ##send Notification on-site 

        ##send Gmail message 

        return redirect (reverse ('rooms:property_detail', kwargs={'slug':self.object.slug}))


class NewProperty(CreateView):
        model = models.Room
        fields = ['name','price','description','location','image','category']

        def post(self, request, *args, **kwargs): #to add post function of the form to the database
            form = self.get_form()
            if form.is_valid():
                myform = form.save(commit=False)
                myform.owner = request.user #myform here is an a form parent to the form fields
                myform.save() #myform here is the main form of adding rooms
                
                return redirect (reverse('rooms:property_list'))

            

