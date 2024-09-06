from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
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