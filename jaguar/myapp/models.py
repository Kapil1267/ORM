from django.db import models
from django.contrib import admin
class vehicle_detail(models.Model):
    vehicle_number=models.CharField(max_length=8)
    company=models.CharField(max_length=14)
    year=models.IntegerField()
    phone_number=models.IntegerField(primary_key=True)
    address=models.TextField()
    Email=models.EmailField()
    owner_name=models.CharField(max_length=30)
class vehicle_detailAdmin(admin.ModelAdmin):
    list_display=['vehicle_number','company','year','phone_number','address','Email','owner_name']
