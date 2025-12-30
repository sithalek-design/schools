from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *

def mainprogram(request):
    mainprogramform=MainProgramForm()
    context={
        'mainprogramform':mainprogramform,
    }
    return render(request,'mainprogram.html',context)
def mainprogram_data(request):
    if request.method=='POST':
        mpprogramkh=request.POST['mpprogramkh']
        mpprogramen=request.POST['mpprogramkh']
        abbreviation=request.POST['abbreviation']
        mainprogram=MainProgram(mp_name_kh=mpprogramkh,mp_name_en=mpprogramen,abbreviation=abbreviation)
        mainprogram.save()
        return HttpResponse("Save done!")

def subprogram(request):
    return render(request,'subprogram.html')
