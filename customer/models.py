from django.db import models

# Create your models here.

class Customer (models.Model):
    names = models.CharField(max_length=32)
    phone_number = models.IntegerField()
    email =models.EmailField()
    adress=models.TextField()

    def __str__(self):
        return self.names


