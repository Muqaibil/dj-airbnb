from django.db import models

# Create your models here.
class About(models.Model):
    what_we_do = models.TextField(max_length=1000)
    goal = models.TextField(max_length=1000)
    mission = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='about/')

    
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

class FAQ(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
       
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    