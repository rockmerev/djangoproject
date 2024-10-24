from django.shortcuts import render
from . import forms
from . import models

from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def home(request):
    if request.method=="POST":
        x=0
        form=forms.homeform(request.POST)
        un=request.POST['fname']
        up=request.POST['fpass']
        #return HttpResponseRedirect(f"login\{un}&{up}")
        try:
            x=models.store.objects.filter(fname=un,fpass=up)
            if x:
                return render(request,'tq.html',{"text":"LOGIN SUCCESSFULL"})
            else:
                return render(request,'tq.html',{"text":"LOGIN INVALID"})
        except:
            x=0
            return render(request,'tq.html',{"text":"LOGIN INVALID"})
    return render(request,"index.html",{'form':forms.homeform})


def tq(request):
    return render(request,"tq.html")

def signupp(request):
    
    if request.method=='POST':
        form=forms.homeform(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST['fname'])
            return render(request,'tq.html',{"text":"YOU ARE REGISTERED!! YOU CAN LOGIN"})
    return render(request,"signup.html",{'form':forms.homeform})

def login(request):
    return render(request,"Login.mhtml")