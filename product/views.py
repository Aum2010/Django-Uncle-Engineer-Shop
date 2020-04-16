from django.shortcuts import render
from django.http import HttpResponse
from .models import AllProduct

# Create your views here.
def Home(request):
    # return HttpResponse('<h1>Hello World</h1>')
    return render(request,'product/home.html')

def About(request):
    return render(request,'product/about.html')

def Mobile(request):
    allProduct = AllProduct.objects.all()
    context = {'allproduct' : allProduct}
    return render(request,'product/mobile.html' ,context)
