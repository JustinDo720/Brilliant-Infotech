from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from .forms import StudentForm
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