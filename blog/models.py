from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Post(models.Model):
    title = models.CharField(_('title'), max_length=50)
    tags = TaggableManager(_('tags'))
    image = models.ImageField(_('image'), upload_to='post/')
    created_at = models.DateTimeField(_('creared at'), default=timezone.now)
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE, verbose_name=_('author'))
    viwe_count = models.IntegerField(_('view count'), default=0)
    category = models.ForeignKey('Category', related_name='post_category', on_delete=models.CASCADE, verbose_name=('category'))
    content = models.TextField(_('content'), null=True, blank=True)
    #we can use verbose_name of "_" for translation..
    #we use "_" with the name of field directly at the begining when there is no relation with other tables
    #we use verbose_name for translation when we have a forign key at the end..


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
