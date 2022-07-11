from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Students Model 
class Student(models.Model):
    """ Each user will link by default with one student object """
    # OneToOneField to link each django user with an student user by default
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='defatul.png', upload_to='avatar')
    stripe_customer_id = models.CharField(blank=True, null=True, max_length=100)

    def __str_(self):
        # accesing the username of the user object. created by default with django auth.
        return self.user.username

# class Pricing(models.Model):
#     """ Each pricing object correspond to a pricing plan of Stripe and each 
#     Course can have differents pricing """
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100, blank=True, unique=True)
#     stripe_price_id = models.CharField(max_length=100, blank=True)
#     price = models.DecimalField(decimal_places=2, max_digits=5)
#     currency = models.CharField(max_length=10)

#     def __str__(self):
#         return self.name

# class Subscription(models.Model):
#     """ Each student will have a corresponding subscription, and the Pricing 
#     object may have multiple subscriptions """
#     student = models.OneToOneField(Student, on_delete=models.CASCADE)
#     pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE, related_name='subscriptions') # related name is to acces the subscriptions and the Pricing object
#     stripe_subscription_id = models.CharField(max_length=100, blank=True)
#     status = models.CharField(max_length=100)

#     def __str__(self):
#         return self.student.user.email


# As son as the student is created, this will create a corresponding subscription for that student
def post_save_student_create(sender, instance, created, *args, **kwargs):
    # if statement to check if the create parameter is true  which meanst that the user object has been created
    if created:
        # create a student subscription
        student = Student.objects.create(user=instance)
        # get the pricing object with the name of Free, and assign the object to a variable called:(free_pricing)
        free_pricing = Course.objects.get(name='Free')
        # Then create the subscripton with the pricing fiels is the free_pricing variable 
        subscription = Subscription.objects.create(student=student, pricing=free_pricing) 
        # the subscription sutend paramaters are the paramter that ust have been created
        customer = stripe.Customer.create(
            email=instance.email
        )
        # Create the subscription 
        customer_subscription = stripe.Subscription.create(
            customer=customer['id'],
            items=[
                {
                    'price': 'price_1LIDIdIlGY9kiyMaHLpbquPL'
                }
            ],
        )
        print(customer_subscription)
        subscription.status = customer_subscription["status"]
        subscription.stripe_subscription_id = customer_subscription["id"]
        student.stripe_customer_id = customer["id"]
        student.save()
        subscription.save()

def pre_save_pricing(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


# To create the student object manually I used the post_save.connect signal, 
# This create an object corresponding with the default user in django
post_save.connect(post_save_student_create, sender=User) # connects the signal with the user model.
# pre_save.connect(pre_save_pricing, sender=Pricing)
