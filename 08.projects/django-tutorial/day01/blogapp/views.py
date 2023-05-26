from django.shortcuts import render
from django.http import HttpResponse

import datetime

posts = [
    {
        "title": "python",
        "author": 'Sivakumar',
        'published': datetime.date.today()
    },
    {
        "title": "Django",
        "author": 'Revanuru',
        'published': datetime.date(day=21, month=12, year=2023)
    },
    {
        "title": "MongoDB",
        "author": 'Moksha',
        'published': datetime.date.today()
    }
]


# Create your views here.
def greet(request):
    context  = {
        'posts': posts,
        'title': 'Page'
    }
    return render(request, 'blogapp/home.html', context)

def about_page(request):
    return render(request, 'blogapp/about.html')
