from django.shortcuts import render
from .form import MyUserCreationForm
from django.contrib.auth import login,logout,authenticate

def registration(request):
    form_user=MyUserCreationForm()
    if request.method=='POST':
        form_user=MyUserCreationForm(request.POST) 
        if form_user.is_valid():
            form_user.save()
      
    context={

        'form_user':form_user
    }

    return render(request,'user.html',context)

def login_user(request):
    print("Login user")
    context={
        'user':'Heloo'
    }
    
    return render(request,'login-user.html',context)
