from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Teacher
from django.db.models import Q

def teacher(request):
    tea=Teacher.objects.all()
    context={'teachers':tea}
    return render(request,'teacher.html',context)

def search(request):
    query=request.GET.get('search','')
    teach=Teacher.objects.filter(
        Q(lname__icontains=query)|Q(fname__icontains=query)
    )
    return render(request,'partials/list-detail.html',{'teachers':teach})
    


