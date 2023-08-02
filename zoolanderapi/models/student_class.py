from django.db import models
from .classroom import Classroom
from .student import Student

class StudentClass(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
