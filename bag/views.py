from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.

def view_bag(request):
    """ A view to return the bag contents page"""

    return render(request, 'bag/bag.html')


def add_one(request, item_id):
    item_id = str(item_id)
    bag = request.session.get('bag', {})
    current_qty = bag.get(item_id, 0)
    bag[item_id] = current_qty+1
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_one(request, item_id):
    item_id = str(item_id)
    bag = request.session.get('bag', {})
   
    current_qty = bag.get(item_id, 0)
    if current_qty < 2:
        del bag[item_id]
    else:
        bag[item_id] = current_qty-1 
    request.session['bag'] = bag
    
    return redirect(reverse('view_bag'))

def remove_item(request, item_id):
    item_id = str(item_id)
    bag = request.session.get('bag', {})
    del bag[item_id]
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    
    if int(item_id) in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
    
    request.session['bag'] = bag
    print('bag is in add', request.session['bag'])
    return redirect(redirect_url)
    