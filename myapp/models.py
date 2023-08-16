from django.db import models

# Create your models here.
class Student (models.Model):
    ism=models.CharField(max_length=350)
    familiya=models.CharField(max_length=500)
    def __str__(self):
        return self.ism