from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from django.conf import settings
# from content.models import Pricing
import stripe

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    """ A cart item object includes some information about a single product
    added to the card (Pricing)"""
    # adding a table 
    # pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    
    def sub_total(self):
        return self.pricing.price * self.quantity


    def __str__(self):
        return self.pricing