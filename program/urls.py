from django.urls import path
from . import views

urlpatterns=[
    
    path('main-program/',view=views.mainprogram,name='main-program'),
    path('main-program-save/',view=views.mainprogram_save,name='main-program-save'),
    path('main-program-data/',view=views.mainprogram_data,name='main-program-data'),
    path('sub-program/',view=views.subprogram,name='sub-program'),
    

]