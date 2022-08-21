from django.urls import path
from . import views

# Login Register and logout URLS
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),

]
