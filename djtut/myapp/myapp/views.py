from django.http import HttpResponse
import datetime
from django.shortcuts import render
def home(request):
    date=datetime.datetime.now()
    return render(request,"home.html",{})
    # return HttpResponse("<h1>Hello this is index page </h1>"+str(date))

def about(request):
    return render(request,"about.html",{})
    # return HttpResponse("<h1>this is about page </h1>")

def services(request):
    return render(request,"service.html",{})
    # return HttpResponse("<h1>This is services page </h1>")