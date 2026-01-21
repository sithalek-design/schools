from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Teacher(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    dob=models.DateField(null=True,blank=True)
    # teacher_image=models.ImageField(upload_to='imgs/profiles/teacher/',null=True,blank=True)
    teacher_image = CloudinaryField(
        'teacher_image',
        folder='teacherProfile',
        null=True,
        blank=True
    )

    created_at=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.fname} {self.lname}"
