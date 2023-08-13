from django.db import models

# Create your models here.
class Vendors(models.Model):
    first_name=models.CharField(max_length=32)
    second_name=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=16)
    
