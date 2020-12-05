from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    tags = TaggableManager()
    image = models.ImageField(upload_to='post/')
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    viwe_count = models.IntegerField(default=0)
    category = models.ForeignKey('Category', related_name='post_category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
