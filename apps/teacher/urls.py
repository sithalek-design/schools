from django.urls import path
from . import views

urlpatterns=[
    
    path('teacher/',view=views.teacher,name="teacher"),
    path('search/',view=views.search,name="search"),
    

]