from django.db import models
from django.contrib import admin
class Vehicle_DB(models.Model):
    reg_no=models.IntegerField()
    name=models.CharField(max_length=28)
    address=models.TextField()
    campany=models.CharField(max_length=10)
    model=models.CharField(max_length=10)
    licence_num=models.CharField(max_length=10,primary_key=True)
    num_plate=models.IntegerField()
class Vehicle_DBAdmin(admin.ModelAdmin):
    list_display=["reg_no","name","address","campany","model","licence_num","num_plate"]


# Create your models here.
