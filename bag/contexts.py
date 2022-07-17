from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from content.models import Course

def bag_contents(request):

    bag_item = []
    total = 0 
    product_count = 0
    bag = request.session.get('bag', {})

    # for course, quantity in bag.items():
    #     course = get_object_or_404(Course, pk=course.id)
    #     total += quantity * course.price
    #     bag_items.append({
    #         'item_id': course.id,
    #         'quantity': quantity,
    #         'course': course,
    #     })

    context = {

        'bag_item': bag_item,
        'total': total, 
        'product_count': product_count,

    }
    
    return context