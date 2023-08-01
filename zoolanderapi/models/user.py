from django.db import models

class User(models.Model):
    """Model that represents a user"""
    name = models.CharField(max_length=50)
    uid = models.CharField(max_length=50)
