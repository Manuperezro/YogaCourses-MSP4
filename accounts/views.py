from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UpdateProfileForm
from django.contrib.auth.decorators import login_required

#Login Register and Logout Functions
def login(request):

    # I add this first if to redirect the user to the courses list page when logout. 
    if request.user.is_authenticated:
        return redirect('course-list')


    if request.method == "POST":
        # get form input values
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('You are now logge in')
            return redirect('course-list')
        
        print('Invalid credentials')
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
            return redirect('register') 
        if User.objects.filter(username=username).exists():
            # that username is taken
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            # that email is being used
            return redirect('register')
        
        user = User.objects.create_user(username=username, email=email, password=password_1, first_name=first_name, last_name=last_name)
        user.save()
        # Your are now register and can login
        return redirect('login')

    return render(request, 'accounts/register.html')


#Logout dont render any template, simply will navigate to the course list url.
def logout(request):
    auth.logout(request)
    return redirect('course-list')


# my profile users allows users to change information and the avatar img in their files.
@login_required(login_url='/accounts/login')
def my_profile(request):

    # if not request.user.is_authenticated:
    #     return redirect('login')

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

    student_form = UpdateProfileForm(instance=request.user.student)

    context = {
        'student': request.user.student,
        'student_form': student_form
    }

    return render(request, 'accounts/my_profile.html', context)