from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from django.conf import settings
from content.models import Course
import stripe

# Create your models here.

# class CartAbstract(models.Model):
#      user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#      created = models.DateTimeField(auto_now=True)
#      updated = models.DateTimeField(auto_now=True)

#      class Meta:
#         abstract = True


# class CartItem(CartAbstract):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=0)

#     def __str__(self):
#         return f"{self.course.name} : {self.quantity}"

    
# class Cart(CartAbstract):
#     items = models.ManyToManyField(CartItem)
#     total_items = models.IntegerField(default=0)
#     total_price = models.FloatField(default=0)

#     def __str__(self):
#         return f"{self.user.username},  {self.id}"
