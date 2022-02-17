from django.db import models
from django.conf import settings

# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)
from autoslug import AutoSlugField


# Create your models here.
class Category(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='categories', on_delete=models.DO_NOTHING)

    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name',
                         unique_with=['id'])
    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'{self.slug}/'


