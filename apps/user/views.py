from django.shortcuts import render
from .form import MyUserCreationForm

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

# Create your views here.
