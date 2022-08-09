from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<int:item_id>', views.add_to_bag, name='add_to_bag'),
    path('add_one/<int:item_id>', views.add_one, name='add_one'),
    path('remove_one/<int:item_id>', views.remove_one, name='remove_one'),
    path('remove_item/<int:item_id>', views.remove_item, name='remove_item'),
]
