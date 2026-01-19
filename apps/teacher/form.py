from django.forms import ModelForm, forms
from .models import *


   



class TeacherForm(ModelForm):
    class Meta:
        model=Teacher
        fields="__all__"
        # fields=['mp_name_kh','mp_name_en','abbreviation']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['fname'].widget.attrs.update({'class':'form-control','placeholder': 'Enter in FName','id':'txtfname_save','autocomplete': 'off'})
        self.fields['lname'].widget.attrs.update({'class':'form-control','placeholder': 'Enter in LName','id':'txtlname_save'})
        self.fields['dob'].widget.attrs.update({
                'class': 'form-control datepicker',
                'placeholder': 'YYYY-MM-DD',
                'autocomplete': 'off'
            })
        self.fields['teacher_image'].widget.attrs.update({
                'class': 'form-control'
            })




        
        
        
        
      
