from django.db import models
from io import BytesIO
from PIL import Image
from categories.models import Category

from django.core.files import File
from django.conf import settings
from autoslug import AutoSlugField
# Create your models here.

class Product(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='products', on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name',
                         unique_with=['id'])
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
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

