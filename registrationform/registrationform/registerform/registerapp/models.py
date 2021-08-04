from django.db import models

# Create your models here.
class regmode(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.IntegerField()
    password = models.CharField(max_length=50)
    conpassword = models.CharField(max_length=50)
