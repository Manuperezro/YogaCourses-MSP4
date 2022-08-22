from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UpdateProfileForm
from django.shortcuts import get_object_or_404

from checkout.models import Order

from .models import Student
from .forms import UpdateProfileForm

# Login Register and Logout Functions


def login(request):

    # I add this first if to redirect the user to the courses list page when logout.
    if request.user.is_authenticated:
        return redirect('course-list')

    if request.method == "POST":
        # get form input values
        username = request.POST['username']
        password = request.POST['password']

        # Authentificated the users username and password
        user = auth.authenticate(username=username, password=password)

        # I f the user variable exists then log in to this
        # account using the (auth.login) funtion
        if user is not None:
            auth.login(request, user)
            # Once loged in navigate to the course list
            return redirect('course-list')

        else:
            messages.success(request, "There was an Error in the Login, Please Try again")
            return redirect('login')

    return render(request, 'accounts/login.html')


def register(request):

    if request.user.is_authenticated:
        return redirect('course-list')

    if request.method == "POST":
        # get form input values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']

        if password_1 != password_2:
            # Passwords don't match
            messages.success(request, "Passwords Don't match")
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            # that username is taken
            messages.success(request, "Username already exists")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.success(request, " The email is already in use, try with a different email")
            # that email is being used
            return redirect('register')

        # If username and email doesn't exist in the database, create a
        # new user with the user variable and saving called the  with the save method.
        user = User.objects.create_user(username=username, email=email, password=password_1, first_name=first_name, last_name=last_name)
        user.save()
        # Once register is succesfull navigate to the login page
        # Your are now register and can login
        return redirect('login')

    return render(request, 'accounts/register.html')


# Logout dont render any template, simply will navigate to the course list url.
def logout(request):
    """ This function redirect to the course list view """
    auth.logout(request)
    return redirect('course-list')


# my profile users allows users to change information and the avatar img in their files.
@login_required(login_url='/accounts/login')
def my_profile(request):

    # if not request.user.is_authenticated:
    #     return redirect('login')
    profile = get_object_or_404(Student, user=request.user)

    if request.method == 'POST':
        user = request.user
        user.email = request.POST['email']
        user.username = request.POST['username']
        student_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.student)

        if student_form.is_valid():
            student_form.save()
            user.save()
            # Your account have been updated!
            return redirect('my_profile')
    
    orders = profile.orders.all()
    student_form = UpdateProfileForm(instance=request.user.student)

    context = {
        'student': request.user.student,
        'orders': orders,
        'student_form': student_form
    }

    return render(request, 'accounts/my_profile.html', context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    print("Order is", order)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, template, context)
