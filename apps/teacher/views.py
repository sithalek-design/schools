from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Teacher
from django.db.models import Q
from .form import *

def teacher(request):
    tea=Teacher.objects.all().order_by()
    context={'teachers':tea}
    return render(request,'teacher.html',context)

def search(request):
    import time
    time.sleep(2)
    query=request.GET.get('search','')
    teach=Teacher.objects.filter(
        Q(lname__icontains=query)|Q(fname__icontains=query)
    )
    return render(request,'partials/list-detail.html',{'teachers':teach})

def update_form(request,pk):
    tea=Teacher.objects.get(id=pk)
    form=TeacherForm(instance=tea)

    context={
        'tForm':form,
    }
    # context={'teachers':tea}
    
    return render(request,'update_form.html',context)
    


