from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Room(models.Model):
    owner = models.ForeignKey(User, related_name='room_owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(max_length=10000)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='property/')
    category = models.ForeignKey('Category', related_name='room_category', on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)




    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify (self.name)
        super(Room, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse ('rooms:property_detail', kwargs={'slug':self.slug})

    def __str__(self):
        return self.name

   

class RoomImage(models.Model):
    room = models.ForeignKey(Room, related_name='room_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_image/')

    def __str__(self):
        return str(self.room)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class RoomReview(models.Model):
    room = models.ForeignKey(Room, related_name='room_review', on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    feedback = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.room)


class RoomBook(models.Model):
    room = models.ForeignKey(Room, related_name='room_book', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    from_date = models.DateField(default=timezone.now)
    to_date = models.DateField(default=timezone.now)
    guest = models.IntegerField(default=1)
    childern = models.IntegerField(default=0)

    def __str__(self):
        return self.name