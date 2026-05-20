from django.urls import path
from . import views

urlpatterns=[
    
    path('building/',view=views.building,name='building'),
    
    

]