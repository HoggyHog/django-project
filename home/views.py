import math
from django.shortcuts import render,HttpResponse
from home.models import Contact

def index(request):
    if(request.method=="POST"):
        name=request.POST.get('name')
        email=request.POST.get('email')
        roll=request.POST.get('roll')
        phone=request.POST.get('phone')
        dept=request.POST.get('dept')

        web=request.POST.get('web')
        ui=request.POST.get('ui')
        business=request.POST.get('business')

        comments=request.POST.get('comments')

        if(len(phone)==10):
            contact=Contact(name=name,email=email,roll=roll,phone=phone,dept=dept,web=web,ui=ui,business=business,comments=comments)
            contact.save()
        else:
            return render(request,'index.html',{'error':True})

        

    return render(request,'index.html')