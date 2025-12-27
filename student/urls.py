from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,),
    path('student/',view=views.student,name='student'),
    path('student_data/',view=views.student_data,name='student_data'),
    path('test/',view=views.test)

]