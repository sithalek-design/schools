from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('student/',view=views.student),
    path('test/',view=views.test)

]