from django.urls import path
from . import views

urlpatterns=[
    
    path('user/',view=views.registration,name="user"),
    path('login_form/',view=views.login_form,name="login_form"),
    path('login/',view=views.login_user,name="login"),
    path('logout/',view=views.logout_user,name="logout"),

    

]