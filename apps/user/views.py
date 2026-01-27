from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm

def registration(request):
    form_user=UserChangeForm()
    context={

        'form_user':form_user
    }

    return render(request,'user/index.html',context)

# Create your views here.
