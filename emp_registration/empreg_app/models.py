from django.db import models

# Create your models here.
class EmpReg(models.Model):
    emp_id = models.IntegerField()
    name = models.CharField(max_length=20)
    dept = models.CharField(max_length=20)
    