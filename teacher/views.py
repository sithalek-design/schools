from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def teacher(request):
    return render(request,'teacher.html')
