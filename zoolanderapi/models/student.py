from django.db import models

class Student(models.Model):
    student_full_name: models.CharField(max_length=100)
    age: models.IntegerField()
    image_url: models.CharField(max_length=200)
