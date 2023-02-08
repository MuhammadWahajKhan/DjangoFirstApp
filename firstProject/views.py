from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from urllib.parse import urlencode

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

def thankyou(request):
    if request.method=="GET":
        data = request.GET.dict()
    return render(request, 'thankyou.html',{'data':data})    

def contact(request):
    data={}
    try:
        if request.method=='POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            subject=request.POST.get('subject')
            message=request.POST.get('message')

            data={
                'name':name,
                'email':email,
                'subject':subject,
                'message':message
            }

            url = "/thankyou/?{}".format(urlencode(data))

            return HttpResponseRedirect(url)
    except:
        pass    
    return render(request, 'contact.html',data)
   