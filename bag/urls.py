from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('cart/add/<int:stripe_price_id', views.add_cart, name='add_cart'),
    path('cart/', views.cart, name='shopping_cart'),

]