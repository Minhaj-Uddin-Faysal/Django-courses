from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.CharField()
    # avatar=models.ImageField(upload_to='avatars/',blank=True,null=True)
    birth_date=models.DateField(blank=True,null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

