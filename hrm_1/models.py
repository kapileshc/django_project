from django.db import models

# Create your models here.

class Employee(models.Model):
    firstName =models.CharField(max_length=50, blank=True, default='')
    lastName = models.CharField(max_length=50, blank=True, default='')
    designation = models.CharField(max_length=50)

class Attendance(models.Model):
    date = models.DateField(auto_now_add=True)
