from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Course, Video, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY

products = stripe.Product.list()
prices = stripe.Price.list()

# def get_stripe_products():
#     for product in products.data:
#         obj, _ = Course.objects.get_or_create(name=product.name)
#         price_ = [x for x in prices.data if x.product == product.id][0] 
#         price = float(price_.unit_amount/ 100)
#         obj.price = price
#         image_ = [y for y in images.data if y.product == product.id][0]
#         obj.image = image
#         active_ = [z for z in prices.data if z.product == product.id][0]
#         obj.price = avtive

	# Set the object image to the one on Stripe

	# Set the object active to the one Stripe
        

class CategoryDetailView(DetailView):
    """ This class is to display the list Categories """
    model = Category
    template_name = "content/category_detail.html"

def view_home(request):
    """ A view to return the home page"""

    return render(request, 'content/home.html')

# def view_home(request, category_slug=None):
#     """ A view to return the home page"""
#     category_page = None
#     courses = None
#     if category_slug != None:
#         category_page = get_object_or_404(Category, slug=category_slug)
#         courses = Course.objects.filter(category=category_page, avalaible=True)
#     else:
#         courses = Course.objects.all().filter(avalaible=True)
#     return render(request, 'content/home.html' {'category': category_page, 'courses' : courses})
    
    return render(request, 'content/home.html')


class CourseListView(ListView):
    """ This class iherit the listView class which means it will have built 
    in features to return a list of objects of a model. """
    # Assign it the Course class to the model variable, because the course 
    # list view inherits from the listView so it will automaticly 
    # return the list of course objects to an array call object_list by default
    model = Course
    template_name = "content/course_list.html"

    # query to tell the class CourseListView which data need to return, but 
    # updating the model variable is more concise, assign it the Course class  
    # to it: (queryset = Course.objects.all())

class CourseDetailView(DetailView):
    model = Course
    template_name = "content/course_detail.html"

# I used LoginRequiredMixin here so when students try to acces for a Course
# That required a subscription payment will redirect the user to the Login view. 
class VideoDetailView(LoginRequiredMixin, DetailView):     # CoursePermissionMixin as a parameter
    model = Video
    template_name = "content/video_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = get_object_or_404(Course, slug=self.kwargs["course_slug"])
        context['course'] = course

        return context

