from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Teacher
from django.db.models import Q
from .form import *

def teacher(request):
    tform=TeacherForm()
    tea=Teacher.objects.all().order_by()
    context={'teachers':tea,
             'tForm':tform,
             }
    return render(request,'teacher.html',context)

def create(request):
    # if request.method=='POST':
    #     print(request)
        # return render(request,'m.html')
    print("Hello")

def search(request):
    import time
    time.sleep(2)
    query=request.GET.get('search','')
    teach=Teacher.objects.filter(
        Q(lname__icontains=query)|Q(fname__icontains=query)
    )
    return render(request,'partials/detail-list_teacher.html',{'teachers':teach})

def update_form(request,pk):
    tea=Teacher.objects.get(id=pk)
    form=TeacherForm(instance=tea)

    context={
        'tForm':form,
    }
    # context={'teachers':tea}
   
    return render(request,'partials/update-form_teacher.html',context)
    


