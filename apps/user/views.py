from django.shortcuts import render,redirect
from .form import MyUserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login')
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


def login_form(request):
    print("Login Rorm")
    context={
        'user':'Heloo'
    }
    
    return render(request,'login-user.html',context)

# def login_user(request):
#     if request.user.is_authenticated:
#         return redirect('home')

#     if request.method=='POST':
#         myusername=request.POST.get('username')
#         mypassword=request.POST.get('password')

#         user_login=authenticate(request,username=myusername,password=mypassword)
#         if user_login is not None:
#             return redirect('user')
#         else:
#             print("Not you")
#             return redirect('login_form')
#     context={
#         'user':'Heloo'
#     }
    
#     return render(request,'login-user.html',context)

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        myusername = request.POST.get('username')
        mypassword = request.POST.get('password')

        user_login = authenticate(
            request,
            username=myusername,
            password=mypassword
        )

        if user_login is not None:
            login(request, user_login)   # ✅ THIS IS REQUIRED
            return redirect('user')
        else:
            messages.info(request,f'Please check your UserName or Password again!')
            return redirect('login_form')

    return render(request, 'login-user.html')


def logout_user(request):
    logout(request)
    return redirect('login_form')