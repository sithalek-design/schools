from django.urls import path
from . import views

urlpatterns=[
    
    path('teacher/',view=views.teacher,name="teacher"),
    path('search/',view=views.search,name="search"),
    path('update/<int:pk>',view=views.update_form,name="update"),
    path('create',view=views.create,name="create-teacher"),
    
    

]