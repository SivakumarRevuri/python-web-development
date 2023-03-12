from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function based views
def html_view(request):
    d = {}
    d['name'] = 'Sivakumar'
    d['profession'] = 'Software Engineer'
    
    response = f'<h1> Employee name: {d["name"]} and his profession is: {d["profession"]} </h1>'
    
    return HttpResponse(response)

import json
def json_view(request):
    d = {}
    d['name'] = 'Sivakumar'
    d['profession'] = 'Software Engineer'
    json_resp = json.dumps(d)
    
    return HttpResponse(json_resp, content_type='application/json')

# the above approach is more recommended because json is an internal module of python, while
# JsonResponse is from django.
from django.http import JsonResponse
def json_view2(request):
    d = {
        'address': 'Bangalore',
        'salary': 80000
    }
    d['name'] = 'Sivakumar'
    d['profession'] = 'Engineer Graduate'
        
    return JsonResponse(d)

# class based views are as follows
from django.views.generic import View

class EmployeeClassBasedView(View):
    def get(self, request, *args, **kwargs):
        print('Get method is called!!!')
        emp_data = {'msg': 'Your message comes here'}
        return JsonResponse(emp_data)
    
    def post(self, request, *args, **kwargs):
        print('post method is called!!!')
        emp_data = {'msg': 'Your message comes here'}
        json_data = json.dumps(emp_data)
        return HttpResponse(json_data, 'application/json')
    
    def put(self, request, *args, **kwargs):
        print('put method is called!!!')
        emp_data = {'msg': 'Your message comes here'}
        return JsonResponse(emp_data)
    
    def delete(self, request, *args, **kwargs):
        print('delete method is called!!!')
        emp_data = {'msg': 'Your message comes here'}
        return JsonResponse(emp_data)
