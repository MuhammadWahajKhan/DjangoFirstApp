from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data={
        'title':'Home',
        'body':'Welcome To Home Page',
        'courses':['Laravel', 'Django', 'Next JS'],
        'age':'18',
        'employee_details':[
            {'first_name':'Muhamamd', 'last_name':'Wahaj Khan'},
            {'first_name':'Ali', 'last_name':'Rehman'},
        ]
    }
    return render(request, 'index.html', data)

def aboutUs(request):
    return HttpResponse('About Us')

def courses(request):
    return HttpResponse('Courses')

def courseDetails(request, courseid):
    return HttpResponse(courseid)    