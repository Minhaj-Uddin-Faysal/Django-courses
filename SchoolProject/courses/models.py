from django.db import models
from Teachers.models import Teacher
# Create your models here.
class Courses(models.Model):
    name=models.CharField(max_length=30)
    code=models.CharField( max_length=10)
    teacher=models.ForeignKey(Teacher, on_delete=models.SET_NULL,null=True,related_name='courses')
    