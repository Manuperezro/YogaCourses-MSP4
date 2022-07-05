from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view to return the bag contents page"""

    return render(request, 'bag/bag.html')


def subscription_type(request):
    """ A view to return the subscription types and Prices """

    return render(request, 'bag/subscription.html')