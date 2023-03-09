from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def greet_func(request):
    return HttpResponse('<h1>Hello this is a response for your request.</h1>')


def display_date(request):
    result = "<h1>Today's date is: "+ str(datetime.now()) + "</h1>"
    return HttpResponse(result)

def wish_user(request):
    dt = str(datetime.now())
    my_dict = {'date': dt}
    return render(request, 'testapp/wish.html', context=my_dict)