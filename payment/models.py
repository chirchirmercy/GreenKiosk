from django.db import models

# Create your models here.

class Payment (models.Model):
    payment_status =models.CharField(max_length=16)
    payment_method = models.CharField(max_length=32)
    expiration_date = models.DateField(max_length=20)

    def __str__(self):
        return self.payment_status






