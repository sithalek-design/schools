from django.forms import ModelForm
from .models import *

class TeacherForm(ModelForm):
    class Meta:
        model=Teacher
        fields="__all__"
        # fields=['mp_name_kh','mp_name_en','abbreviation']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['fname'].widget.attrs.update({'class':'form-control','placeholder': 'Enter in FName','id':'txtfname_save'})
        self.fields['lname'].widget.attrs.update({'class':'form-control','placeholder': 'Enter in LName','id':'txtlname_save'})
      
