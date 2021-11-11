from django.db import models

# Create your models here.

class Account(models.Model):
    statement=models.CharField(max_length=100)
    grouping=models.CharField(max_length=150)
    grouping_label=models.CharField(max_length=200)
    account_name=models.CharField(max_length=250)
    account_name_label=models.CharField(max_length=200)
    context=models.CharField(max_length=50)
    value=models.IntegerField()
    unit=models.CharField(max_length=50)