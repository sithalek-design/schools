
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

def building(request):
    context={
        'ss':"sdfa"
        }
    return render(request,"building.html",context)

