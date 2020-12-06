from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Post, Category

class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin): 
    #Why did we put summernot before admi.modeladmin??
    #This customized admin is created to merge more than a model registeration into one page. 

    summernote_fields = ('content')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)