from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Data(models.Model):
    ItemName    =   models.CharField(max_length=100)
    SubItemName =   models.CharField(max_length=100)
    UnitName    =   models.CharField(max_length=50)
    Weight      =   models.IntegerField()
    MaxSingle   =   models.IntegerField()
    
