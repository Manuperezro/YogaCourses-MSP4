from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.conf import settings
import stripe

from django_countries.fields import CountryField

stripe.api_key = settings.STRIPE_SECRET_KEY


# Students Model
class Student(models.Model):
    """ Each user will link by default with one student object """
    # OneToOneField to link each django user with an student user by default
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    avatar = models.ImageField(default='defatul.png', upload_to='avatar')
    stripe_customer_id = models.CharField(blank=True, null=True, max_length=100)

    def __str_(self):
        # accesing the username of the
        # user object. created by default with django auth.
        return self.user.username


def post_save_student_create(sender, instance, created, *args, **kwargs):
    if created:
        Student.objects.create(user=instance)

post_save.connect(post_save_student_create, sender=User)
