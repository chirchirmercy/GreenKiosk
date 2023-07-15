from django.db import models

# Create your models here.
class Register_account (models.Model):
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    password=models.CharField(max_length=24)
    email=models.EmailField(max_length=20)
    phone_number=models.CharField(max_length=16)
    adress=models.CharField(max_length=30)
    
