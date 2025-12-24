from django.db import models

# Create your models here.

class Student(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)



    def __str__(self):
        return self.fname

