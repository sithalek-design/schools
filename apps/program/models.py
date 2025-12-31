from django.db import models
from django.forms import ModelForm

class MainProgram(models.Model):
    mp_name_kh=models.CharField(max_length=200,null=True,blank=True)
    mp_name_en=models.CharField(max_length=200)
    abbreviation=models.CharField(max_length=20,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.mp_name_kh} {self.mp_name_en}"
    

class SubProgram(models.Model):
    su_name_kh=models.CharField(max_length=200,null=True,blank=True)
    su_name_en=models.CharField(max_length=200)
    abbreviation=models.CharField(max_length=20,null=True,blank=True)
    description=models.CharField(max_length=20,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mainprogram=models.ForeignKey(MainProgram, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.su_name_kh} {self.su_name_en}"
    
class MainProgramForm(ModelForm):
    class Meta:
        model=MainProgram
        fields="__all__"
        # fields=['mp_name_kh','mp_name_en','abbreviation']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['mp_name_kh'].widget.attrs.update({'class':'form-control','placeholder': 'Enter in Khmer','id':'txtmpnamekh'})
        self.fields['mp_name_en'].widget.attrs.update({'class':'form-control','placeholder': 'Enter in English','id':'txtmpnameen'})
        self.fields['abbreviation'].widget.attrs.update({'class':'form-control','placeholder': 'Enter abbreviation','id':'txtabbreviation'})