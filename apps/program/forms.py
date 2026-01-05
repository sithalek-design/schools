from django.forms import ModelForm
from .models import *

class MainProgramForm(ModelForm):
    class Meta:
        model=MainProgram
        fields="__all__"
        # fields=['mp_name_kh','mp_name_en','abbreviation']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['mp_name_kh'].widget.attrs.update({'class':'form-control','placeholder': 'Enter in Khmer','id':'txtmpkh_save'})
        self.fields['mp_name_en'].widget.attrs.update({'class':'form-control','placeholder': 'Enter in English','id':'txtmpen_save'})
        self.fields['abbreviation'].widget.attrs.update({'class':'form-control','placeholder': 'Enter abbreviation','id':'txtabbreviatin_save'})
