from django.db import models

# Create your models here.
class SalesRecord (models.Model):
    sales_date=models.DateField(max_length=40)
    amount=models.DecimalField(max_digits=8,decimal_places=2)
   