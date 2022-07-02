from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Students Model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='defatul.png')
    # ,update_to='avatar'
    stripe_customer_id = models.CharField(blank=True, null=True, max_length=100)

    def __str_(self):
        return self.user.username

def post_save_student_create(sender, instance, created, *args, **kwargs):
    if created:
        Student.objects.create(user=instance)

post_save.connect(post_save_student_create, sender=User)