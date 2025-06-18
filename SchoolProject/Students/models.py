from django.db import models
from courses.models import Courses
# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField( unique=True)
    enrolled_courses=models.ManyToManyField(Courses,related_name='enrolled_students')

    def __str__(self):
        return self.name