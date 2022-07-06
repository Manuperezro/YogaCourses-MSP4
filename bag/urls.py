from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('bag/', views.subscription_type, name='subscription_type'),
]