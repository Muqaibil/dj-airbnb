from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

from . import models


class RoomImageTabular(admin.TabularInline):
    #This is Tabular Admin class is to include a room images model in a tabular view
    #and then merge into the Room admin page
    model = models.RoomImage

class RoomAdmin(SummernoteModelAdmin, admin.ModelAdmin): #Why did we put summernot before admi.modeladmin??
    #This customized admin is created to merge more than a model registeration into one page. 
    #for example, room and roomImages Here

    list_display = ['name','location','price']
    inlines = [RoomImageTabular,] 
    summernote_fields = ('description')
    prepopulated_fields = {'slug': ("name",)}

    #Tabular image container is included in the RoomAdmin page as this class is register and called
    #within the registeration method of model Room.



admin.site.register(models.Room, RoomAdmin) #you can add a class "RoomAdmin fro example" to change the model aspects like display fields etc.
admin.site.register(models.Category)
admin.site.register(models.RoomReview)
admin.site.register(models.RoomBook)
admin.site.register(models.RoomImage)