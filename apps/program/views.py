from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from django.forms.models import model_to_dict
from django.urls import reverse
from .forms import *

def mainprogram(request):
    mainprogramform=MainProgramForm()
    context={
        'mainprogramform':mainprogramform,
    }
    return render(request,'mainprogram.html',context)

def mainprogram_save(request):
    if request.method=='POST':
        # print(request.POST)
        mainprogram=MainProgramForm(request.POST)
        mp=mainprogram.save()
        return JsonResponse(model_to_dict(mp),safe=False)
    
def mainprogram_data(request):
    mainprogram=MainProgram.objects.all()
    return JsonResponse({"mainprogram":list(mainprogram.values())})

def main_program_update_show(request,pk):
    # url=reverse('main-program-show',kwargs={'pk':pk})
    pa=int(pk)
    mainprogram=MainProgram.objects.get(id=pa)
    # return JsonResponse({"mainprogram":MainProgram.objects.all().values()})
    # print(url)
    form=MainProgramForm(instance=mainprogram)

    context={
        'mpForm':form,
    }
    # return JsonResponse({"namekh":mainprogram.mp_name_kh,"nameen":mainprogram.mp_name_en})
    
    # return JsonResponse({"name":"sitha"})
    return render(request,'mainprogram.html',context)
    

def subprogram(request):
    return render(request,'subprogram.html')
