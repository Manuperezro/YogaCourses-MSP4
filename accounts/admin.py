from django.contrib import admin
from .models import Student, Pricing, Subscription

# Register the modals with the admin variable.
admin.site.register(Student)
admin.site.register(Pricing)
admin.site.register(Subscription)