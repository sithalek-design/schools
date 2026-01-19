from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse,JsonResponse
from .models import Teacher
from django.db.models import Q
from .form import *


def teacher(request):
    tform=TeacherForm()
    tea=Teacher.objects.all().order_by('-created_at')


    paginator=Paginator(tea,10)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        page_obj = paginator.get_page(1)
    except EmptyPage:
    # If page is out of range, deliver last page of results.
        page_obj = paginator.get_page(paginator.num_pages)

    context={
             'tForm':tform,
             'button':'Save',
             'teachers':page_obj,
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
    ).order_by('-created_at')
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
    tea=Teacher.objects.get(pk=pk)
    # tea=get_list_or_404(Teacher,pk=pk)
    context={
        'teacher':tea,
        
    }
    return render(request,'partials/modal-content-teacher.html',context)

def run_delete_teacher(request,pk):
    tea=Teacher.objects.get(id=pk)
    tea.delete()
    teacher=Teacher.objects.all().order_by('-created_at')
    return render(request,'partials/detail-list_teacher.html',{'teachers':teacher})

def cancel_button_teacher(request):
    tform=TeacherForm()
    tea=Teacher.objects.all().order_by('-created_at')
    context={'teachers':tea,
             'tForm':tform,
             'button':'Save',
             }

    return render(request,'partials/save-form_teacher.html',context)
    