from django.db import models

class User(models.Model):
    """Model that represents a user"""
    uid = models.CharField(max_length=50)
