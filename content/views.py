from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Course, Video, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.http import HttpResponse
import stripe
import json


stripe.api_key = settings.STRIPE_SECRET_KEY

products = stripe.Product.list()
prices = stripe.Price.list()


class CategoryDetailView(DetailView):
    """ This class is to display the list Categories """
    model = Category
    template_name = "content/category_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Course, slug=self.kwargs["category_slug"])
        context['category'] = category

        return context

    
def view_home(request, category_slug=None):
    """ A view to return the home page"""
    category_page = None
    courses = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.filter(category=category_page)
    else:
        courses = Course.objects.all()
    return render(request, 'content/home.html', {'category': category_page, 'courses' : courses})


def course_list(request):
    new_list = []
    template = "content/course_list.html"
    for product in products.data:
        print('product stripe', product.name)
        obj, _ = Course.objects.get_or_create(name=product.name)
        print('object is ', obj)
        obj.active = product.active
        price_ = [x for x in prices.data if x.product == product.id][0] 
        print('Price is  ', price_.unit_amount)
        price = float(0)
        if price_.unit_amount is None:
            print('price is empty')
            price = float(0)
        else:
            price = float(price_.unit_amount / 100)

        obj.price = price
        print('Stripe Price', price)
        obj.thumbnail = product.images[0] if len(product.images) > 0 else ''
        obj.save()
        new_list.append(obj)

    course = Course.objects.all()
    context = {
        'course': course,
        'products': new_list,
    }
    
    return render(request, template, context)
            

class CourseDetailView(DetailView):
    model = Course
    template_name = "content/course_detail.html"

# I used LoginRequiredMixin here so when students try to acces for a Course
# That required a payment will redirect the user to the Login view. 
class VideoDetailView(LoginRequiredMixin, DetailView):     # CoursePermissionMixin as a parameter
    model = Video
    template_name = "content/video_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = get_object_or_404(Course, slug=self.kwargs["course_slug"])
        context['course'] = course

        return context