from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse,JsonResponse
from .models import Teacher
from django.db.models import Q
from .form import *
import csv
from openpyxl import Workbook

row_number=10
def teacher(request):
    teacher_form=TeacherForm()
    teacher_list=Teacher.objects.all().order_by('-created_at')


    paginator=Paginator(teacher_list,row_number)
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
             'teacher_form':teacher_form,
             'button':'Save',
             'teachers':page_obj,
             }
    return render(request,'teacher.html',context)

def create(request):
    if request.method=='POST':
          form = TeacherForm(request.POST,request.FILES)
          if form.is_valid():
           
           teacher = form.save()
           context= {
                'teacher':teacher
                     }
        #    teacher= Teacher.objects.last()
           
        #    print(teachers)
        # return render(request,'m.html')
            
          return render(request, 'partials/data_row-teacher.html',context)
    

def search(request):
    # import time
    # time.sleep(2)
    query=request.GET.get('search','')
    teacher_list=Teacher.objects.filter(
        Q(lname__icontains=query)|Q(fname__icontains=query)
    ).order_by('-created_at')

    paginator=Paginator(teacher_list,row_number)
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
        'teachers':page_obj
    }

    return render(request,'partials/detail-list_teacher.html',context)

def update_form(request,pk):
    teacher_row_update=Teacher.objects.get(id=pk)
    teacher_form_update=TeacherForm(instance=teacher_row_update)
    old_image=Teacher.teacher_image
    
    if request.method=='POST':
          teacher_form_update = TeacherForm(request.POST,request.FILES,instance=teacher_row_update)
          if teacher_form_update.is_valid():
            
            teacher_form_update.save()
            teacher_list_update=Teacher.objects.all().order_by('-created_at')

            paginator=Paginator(teacher_list_update,row_number)
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
                    'teachers':page_obj
                     }

            return render(request,'partials/detail-list_teacher.html',context)
   
    context={
        'teacher_form':teacher_form_update,
        'button':'Update',
        'id':pk,
        'form_id':'teacher_update_sitha',
    }
    # context={'teachers':tea}
   
    return render(request,'partials/update-form_teacher.html',context)
    
def delete_teacher(request,pk):
    teacher_row_delete=Teacher.objects.get(pk=pk)
    # tea=get_list_or_404(Teacher,pk=pk)
    context={
        'teacher':teacher_row_delete,
        
    }
    return render(request,'partials/modal-content-teacher.html',context)

def run_delete_teacher(request,pk):
    teacher_row_delete=Teacher.objects.get(id=pk)
    teacher_row_delete.delete()
    teacher_list=Teacher.objects.all().order_by('-created_at')

    paginator=Paginator(teacher_list,row_number)
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
            'teachers':page_obj
             }

    return render(request,'partials/detail-list_teacher.html',context)

def cancel_button_teacher(request):
    teacher_form_cancel=TeacherForm()
    tea=Teacher.objects.all().order_by('-created_at')
    context={'teachers':tea,
             'teacher_form':teacher_form_cancel,
             'button':'Save',
             }

    return render(request,'partials/save-form_teacher.html',context)
    

def export_teachers_csv(request):
    response = HttpResponse(
        content_type='text/csv'
    )
    response['Content-Disposition'] = 'attachment; filename="teachers.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Created At'])

    teachers = Teacher.objects.all()

    for t in teachers:
        writer.writerow([
            t.id,
            t.fname,
            t.lname,
            t.created_at.strftime('%Y-%m-%d')
        ])

    return response

def export_selected_teachers_csv(request):
    ids = request.GET.getlist('ids')
    # teachers = Teacher.objects.filter(id__in=ids)
    # print(ids)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="selected_teachers.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name'])

    teachers = Teacher.objects.filter(id__in=ids)
    
    for t in teachers:
      writer.writerow([t.id, t.fname, t.lname])
      print(writer)
    print(response)
    return response

def export_selected_teachers_excel(request):
    ids = request.GET.getlist('ids')
    
    # wb = Workbook()
    # ws = wb.active
    # ws.title = "Teachers"

    # # Header
    # ws.append(['ID', 'First Name', 'Last Name'])

    # teachers = Teacher.objects.filter(id__in=ids)

    # for t in teachers:
    #     ws.append([t.id, t.fname, t.lname])

    # response = HttpResponse(
    #     content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    # )
    # response['Content-Disposition'] = 'attachment; filename=selected_teachers.xlsx'