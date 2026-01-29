from django.urls import path
from . import views

urlpatterns=[
    
    path('user/',view=views.registration,name="user"),
    path('login/',view=views.login_user,name="login"),

    

]