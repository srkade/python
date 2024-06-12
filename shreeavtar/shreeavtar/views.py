from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, World. you are at Home Page")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("Hello, World. you are at About Page")
    

def contact(request):
    return HttpResponse("Hello, World. you are at contact Page")

def service(request):
    return HttpResponse("Hello, World. you are at Services Page")