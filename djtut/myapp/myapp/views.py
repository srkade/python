from django.http import HttpResponse
import datetime
from django.shortcuts import render
def home(request):
    # check=request.GET['check']

    date=datetime.datetime.now()
    isActive=True
    name="learnCodeWithShree"
    list_of_programs=[
        'write a prgram to check even number',
        'write a program to check prime numebr',
        'write a prgram to pring all prime number from 1 to 100',
        'write a program to print pascals triange'
    ]
    student ={
        'name':"Shreee",
        'last_name':"Ade",
        'age':26,
        'education':"Bachelor Of Engineering",
        'address':"Chandan Nagar Pune 411014"

    }
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student,
    }
    return render(request,"home.html",data)
    # return HttpResponse("<h1>Hello this is index page </h1>"+str(date))

def about(request):
    return render(request,"about.html",{})
    # return HttpResponse("<h1>this is about page </h1>")

def services(request):
    return render(request,"service.html",{})
    # return HttpResponse("<h1>This is services page </h1>")