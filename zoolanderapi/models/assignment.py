from django.db import models
from .user import User
from .classroom import Classroom

class Assignment(models.Model):
    """Model that represents a user"""
    teacher_id = models.ForeignKey(User, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    image_url = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
