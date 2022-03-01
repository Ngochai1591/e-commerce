from pydoc import describe
from tabnanny import verbose
from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Category(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='categories', on_delete=models.DO_NOTHING)
    
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to='photos/categories/', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
 

    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'

    def get_image(self):
        if self.image:
            return settings.CURRENT_HOST + self.image.url
        return ''

    