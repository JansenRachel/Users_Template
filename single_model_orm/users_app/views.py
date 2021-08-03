# from re import A
from django.shortcuts import redirect, render
from .models import Users


# Create your views here.
def users_home(request):
    context = {
        'users' : Users.objects.all()
    }
    return render(request, "home.html", context)

def add_user(request):
    firstname = request.POST['firstname']       
    lastname = request.POST['lastname']
    email = request.POST['email']
    age = request.POST['age']
    Users.objects.create (firstname = firstname, lastname = lastname, email = email, age = age)
    return redirect('/')
    
