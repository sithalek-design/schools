
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    # return HttpResponse("my Home")
    return render(request,'home.html')
@login_required(login_url='login')
def student(request):
    return render(request,'index.html')
def student_data(request):
    student=Student.objects.all()
    
    # context={
    #     student:student,
       
    # }

    # data = {'message': 'Hello, world!', 'status': 200}
    # return JsonResponse(data)
    

    return JsonResponse({"student":list(student.values())})
    # return render(request,'index.html',{'student':student})

    return HttpResponse(student)
def test(request):
    return render(request,'main.html')


