from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view to return the bag contents page"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
    
    request.session['bag'] = bag
    print('bag is', request.session['bag'])
    return redirect(redirect_url)

















# def cart(request):
#     """ Shopping cart,  show the produccts before purchase """

#     return render(request, 'bag/cart.html')

# def _cart_id(request):
#     """ Allows users to select products and set the amount that they want to 
#     order and set the information temporarly"""
#     cart = request.session.session_key
#     if not cart:
#         cart = request.session.create()
#     return cart


# def add_cart(request, stripe_price_id):
#     course = Course.objects.get(id=stripe_price_id)
#     try:
#         cart = Cart.objects.get(cart_id=_cart_id(request))
#     except Cart.DoesNotExist:
#         cart = Cart.objects.create(
#             cart_id = _cart_id(request)
#         )
#         cart.save()
#     try:
#         cart_item = CartItem.objects.get(course=course, cart=cart)
#         cart_item.quantity += 1
#         cart_item.save()
#     except CartItem.DoesNotExist:
#         cart_item = CartItem.objects.create(
#             course = course,
#             quantity = 1,
#             cart = cart
#         )
#         cart_item.save()

#     return redirect('cart_detail')

# def cart_detail(request, total=0, counter=0, cart_items= None):
#     try:
#         cart = Cart.objects.get(cart_id=cart_id(request))
#         cart_items = CartItem.objects.filter(cart=cart, active=True)
#         for cart_item in cart_items:
#             total += (cart_items.product.price * cart_item.quantity)
#             counter += cart_item.quantity
#     except ObjectDoesNotExist:
#         pass

#     return render(request, 'bag.html', dict(cart_items=cart_items, total=total, counter=counter))