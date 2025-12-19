

from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("my Home")
def student(request):
    return HttpResponse("Hello world!")
