from django.db import models
from .user import User

class Classroom(models.Model):
    class_name = models.CharField(max_length=50)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
