from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # data={
    #     'title':'Home',
    #     'body':'Welcome To Home Page',
    #     'courses':['Laravel', 'Django', 'Next JS'],
    #     'age':'18',
    #     'employee_details':[
    #         {'first_name':'Muhamamd', 'last_name':'Wahaj Khan'},
    #         {'first_name':'Ali', 'last_name':'Rehman'},
    #     ]
    # }
    return render(request, 'index.html')

def aboutUs(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')
   