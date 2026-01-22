from django.urls import path
from . import views

urlpatterns=[
    
    path('teacher/',view=views.teacher,name="teacher"),
    path('search/',view=views.search,name="search"),
    path('update/<int:pk>',view=views.update_form,name="update"),
    path('create',view=views.create,name="create-teacher"),
    path('delete_teacher/<int:pk>',view=views.delete_teacher,name="delete_teacher"),
    path('run_delete_teacher/<int:pk>',view=views.run_delete_teacher,name="run_delete_teacher"),
    path('cancel_button_teacher/',view=views.cancel_button_teacher,name="cancel_button_teacher"),
    path('export/teachers/csv/', views.export_teachers_csv, name='export_teachers_csv'),
    path('export/teachers/selected/excel/',views.export_selected_teachers_excel, name='export_selected_teachers_excel'),
    

]