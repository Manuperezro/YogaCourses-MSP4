from django.shortcuts import render, redirect

#Login Register and Logout Functions

def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    return render(request, 'accounts/register.html')

#Logout dont render any template, simply will navigate to the course list url.
def logout(request):
    return redirect('course-list')