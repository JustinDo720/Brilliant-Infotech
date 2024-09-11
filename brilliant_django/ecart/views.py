from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from .forms import StudentForm
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login


# Create your views here.

# Request is always mandatory 
def demo(request):
    # Returning an HttpResponse 
    return HttpResponse('<h1>Hello World</h1>')

def demo2(request):
    return render(request, 'demo.html', {'name': 'Thy'})

def squared_num(request):
    num = 5
    return render(request, 'squared.html', {'org_num': num,'sq_num': num**2})

def uppercased(request):
    return render(request, 'uppercased.html', {'word': 'thy'})


def demo3(request):
    context = {
        {'name':'Justin'}, {'name', 'Thy'}
    }
    return render(request, 'demo3.html', context)
    #return render(request, 'demo3.html', {'num': 2, 'name':'Thy', 't_date': date(2024, 9, 6)})


def demo_form(request):
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            student.save()
            return redirect('homepage')
        # if the form isn't valid we'll still render the demo form
        return render(request, 'demo_form.html', {'student':student})
    else:
        # GET request 
        student = StudentForm(request.POST, request.FILES)
        context = {}
        context['student'] = student 
        return render(request, 'demo_form.html', context)


def handle_uploaded_file(file_obj):
    # Uploading the file in chunks 
    with open('ecart/static/upload' + file_obj.name, 'wb+') as des:
        for chunk in file_obj.chunks():
            des.write(chunk)


def user_registration(request):
    if request.method == 'POST':
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']

        user_exists = User.objects.filter(username=username)
        if user_exists.exists():
            return redirect('register')
        # creating new user
        user = User.objects.create_user(first_name=first_name,
                                 last_name=last_name,
                                 username=username,
                                 password=password,
                                 email=email)
        user.save()
        return render(request, 'login.html')
    return render(request, 'user_registration_form.html')

def login_fun(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        if not User.objects.filter(username=username).exists():
            return redirect('login')
        user= authenticate(username=username, password=password)

        if user is None:
            return redirect('register')
        else:
            login(request, user)
            return redirect('homepage')
    return render(request, 'login.html')


def setcookie(request):
    response = HttpResponse("Cookie is Set")
    response.set_cookie('cookie_name', 'cookie_value')
    return response

def getcookie(request):
    # Array
    cookie = request.COOKIES['cookie_name']
    return HttpResponse(cookie)


def cookie_vists(request):
    # Context to add in times_visted
    context = {}

    # Check if we have a cookied called "vists" if not we make one
    # We use get in case of key error
    if request.COOKIES.get('vists', 0):
        # We're going to grab that cookie an increment it by 1 
        vists = request.COOKIES['vists']
        new_vist_val = int(vists) + 1
        context['times_visted'] = new_vist_val
    else:
        # Because this is the first time, we'll set the vists to 1 
        context['times_visted'] = 1

    response = render(request, 'cookie_vists.html', context)
    response.set_cookie('vists', context['times_visted'])
    
    return response

    
    