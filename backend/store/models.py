from tabnanny import verbose
from django.db import models
from django.urls import reverse
from category.models import Category
from django.conf import settings

from io import BytesIO
from PIL import Image
from django.core.files import File


# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',   on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='products', on_delete=models.DO_NOTHING)
    
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='photos/products/image/', blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='photos/products/thumbnail/', blank=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('-created_date', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.images:
            return settings.CURRENT_HOST + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return settings.CURRENT_HOST + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return settings.CURRENT_HOST + self.thumbnail.url

            else:
                return ''
    
    def make_thumbnail(self, image, size=(300,200), quality=85):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=quality)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail