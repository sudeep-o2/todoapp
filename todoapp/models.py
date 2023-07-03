from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(unique=True,null=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task