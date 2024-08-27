from django.http import HttpResponse

import datetime
def test(request):
    date=datetime.datetime.now()
    print("test")
    return HttpResponse("<h1>Hello this is index page </h1>"+str(date))

def about(request):
    return HttpResponse("<h1>this is about page </h1>")

def services(request):
    return HttpResponse("<h1>This is services page </h1>")