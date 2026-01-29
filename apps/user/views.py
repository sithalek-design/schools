from django.shortcuts import render,redirect
from .form import MyUserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

def registration(request):
    form_user=MyUserCreationForm()
    if request.method=='POST':
        form_user=MyUserCreationForm(request.POST) 
        if form_user.is_valid():
            form_user.save()
      
    context={

        'form_user':form_user
    }

    return render(request,'registration-user.html',context)

@login_required(login_url='login')
def login_form(request):
    print("Login Rorm")
    context={
        'user':'Heloo'
    }
    
    return render(request,'login-user.html',context)

def login_user(request):
    if request.method=='POST':
        myusername=request.POST.get('username')
        mypassword=request.POST.get('password')
        user_login=authenticate(request,username=myusername,password=mypassword)
        if user_login is not None:
            return redirect('user')
        else:
            print("Not you")
            return redirect('login_form')
    context={
        'user':'Heloo'
    }
    
    return render(request,'login-user.html',context)

def logout_user(request):
    logout(request)
    return redirect('login_form')