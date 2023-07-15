from django.db import models

# Create your models here.
class Order (models.Model):
    order_number=models.IntegerField()
    order_total=models.FloatField()
    customer=models.TextField()
    date=models.DateField()
    products=models.TextField()
    delivery_date=models.DateField()
    payment_options=models.CharField(max_length=20)


    def __str__(self):
        return self.customer







