from django.db import models

# Create your models here.
class Result(models.Model):
    name = models.CharField(max_length=30)
    rno = models.CharField(max_length=30)
    dob= models.DateField(max_length=30)
    mark = models.IntegerField(max_length=3)
    grade = models.CharField(max_length=2)