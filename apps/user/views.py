from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm

def registration(request):
    form_user=UserCreationForm()
    if request.method=='POST':
        form_user=UserCreationForm(request.POST) 
        if form_user.valid():
            form_user.save()
    

    context={

        'form_user':form_user
    }

    return render(request,'user.html',context)

# Create your views here.
