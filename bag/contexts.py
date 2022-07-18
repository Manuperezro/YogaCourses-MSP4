from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from content.models import Course

def bag_contents(request):

    bag_items = []
    total = 0 
    product_count = 0
    bag = request.session.get('bag', {})

    for course_id, quantity in bag.items():
    # Search the Course table where the primary key is course_id
        print('bag_item:', bag_items)
        course = get_object_or_404(Course, pk=course_id)
        total += quantity * course.price
        bag_items.append({
            'item_id': course_id,
            'quantity': quantity,
            'course': course,
        })


    context = {

        'bag_items': bag_items,
        'total': total, 
        'product_count': product_count,

    }
    
    return context