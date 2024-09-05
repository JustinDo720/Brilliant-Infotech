from django.shortcuts import render
from django.http import HttpResponse
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