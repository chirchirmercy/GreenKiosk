from django.db import models

# Create your models here.
class Delivery(models.Model):
    delivery_person=models.CharField(max_length=100)
    delivery_time=models.DateTimeField()
    delivery_adress=models.CharField(max_length=200)
    destination=models.CharField(max_length=42)