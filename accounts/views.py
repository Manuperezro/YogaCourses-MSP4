from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
#Login Register and Logout Functions

def login(request):
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
    return redirect('course-list')