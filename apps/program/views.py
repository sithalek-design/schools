from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from django.forms.models import model_to_dict

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

def subprogram(request):
    return render(request,'subprogram.html')
