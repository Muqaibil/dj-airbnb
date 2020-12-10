from django.db import models

# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='info/')
    description = models.TextField(max_length=200)
    fb_link = models.URLField(max_length=500)
    twitter_link = models.URLField(max_length=500)
    instgram_link = models.URLField(max_length=500)
    address = models.TextField(max_length=200)
    phone_number = models.CharField(max_length=30)
    mail = models.EmailField(max_length=50)

    class Meta:
        verbose_name =("Info")
        verbose_name_plural = ("Infos")

    def __str__(self):
        return self.name