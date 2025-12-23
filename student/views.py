

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
def home(request):
    # return HttpResponse("my Home")
    return render(request,'home.html')
def student(request):
    return render(request,'index.html')
def test(request):
    return render(request,'main.html')
