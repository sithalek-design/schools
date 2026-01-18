from django.db import models

# Create your models here.

class Teacher(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    dob=models.DateField(null=True,blank=True)
    

    created_at=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.fname} {self.lname}"
