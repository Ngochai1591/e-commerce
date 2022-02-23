from django.db import models
from store.models import Product
from accounts.models import Account

# Create your models here.
class Cart(models.Model):
    owner = models.OneToOneField(Account, on_delete=models.CASCADE ,related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class CartItem(models.Model):
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    cart =  models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)

    def __unicode__(self):
        return '%s: %s' % (self.product.name, self.quantity)


