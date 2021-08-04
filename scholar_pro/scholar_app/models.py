from django.db import models
from django.forms import widgets

# Create your models here.
class Scholar(models.Model):
    name = models.CharField(max_length=20)
    scholar_id = models.IntegerField()
    course = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    id_doc = models.CharField(max_length=20)
    rembursment = models.IntegerField()