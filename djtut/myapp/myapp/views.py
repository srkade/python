from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def home(request):
    isActive = True
    if request.method == 'POST':
        check = request.POST.get("check")  
        print(check)
        if check is None:
            isActive = False
        else:
            isActive = True

    date=datetime.datetime.now()
    
    name="learnCodeWithShree"
    list_of_programs=[
        'write a prgram to check even number',
        'write a program to check prime numebr',
        'write a prgram to pring all prime number from 1 to 100',
        'write a program to print pascals triange'
    ]
    student ={
        'name':"Shreee",
        'age':26,
        'college':"Bachelor Of Engineering",
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