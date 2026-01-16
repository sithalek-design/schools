from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Teacher
from django.db.models import Q
from .form import *

def teacher(request):
    tform=TeacherForm()
    tea=Teacher.objects.all().order_by('-created_at')
    context={'teachers':tea,
             'tForm':tform,
             'button':'Save',
             }
    return render(request,'teacher.html',context)

def create(request):
    if request.method=='POST':
          form = TeacherForm(request.POST)
          if form.is_valid():
           
           teacher = form.save()
        #    teacher= Teacher.objects.last()
           
        #    print(teachers)
        # return render(request,'m.html')
          return render(request, 'partials/data_row-teacher.html',{'teacher':teacher})
    

def search(request):
    # import time
    # time.sleep(2)
    query=request.GET.get('search','')
    teach=Teacher.objects.filter(
        Q(lname__icontains=query)|Q(fname__icontains=query)
    )
    return render(request,'partials/detail-list_teacher.html',{'teachers':teach})

def update_form(request,pk):
    tea=Teacher.objects.get(id=pk)
    form=TeacherForm(instance=tea)
    
    if request.method=='POST':
          form = TeacherForm(request.POST,instance=tea)
          if form.is_valid():
           
            form.save()
            teacher=Teacher.objects.all().order_by('-created_at')
            return render(request,'partials/detail-list_teacher.html',{'teachers':teacher})
   
    context={
        'tForm':form,
        'button':'Update',
        'id':pk,
        'form_id':'teacher_update_sitha',
    }
    # context={'teachers':tea}
   
    return render(request,'partials/update-form_teacher.html',context)
    
def delete_teacher(request,pk):
    tea=Teacher.objects.get(id=pk)
    tea.delete()
    teacher=Teacher.objects.all().order_by('-created_at')
    return render(request,'partials/detail-list_teacher.html',{'teachers':teacher})
    