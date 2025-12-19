

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
def home(request):
    return HttpResponse("my Home")
def student(request):
    return render(request,'index.html')
