from django.db import models

from customer.models import Customer
from cart.models import Cart
from delivery.models import Delivery

# # Create your models here.
class Order (models.Model):
    customers=models.OneToOneField(Customer, null=True, on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    delivery=models.ManyToManyField(Delivery)

    order_number=models.IntegerField()
    order_total=models.FloatField()
    customer=models.TextField()
    date=models.DateField()
    products=models.TextField()
    delivery_date=models.DateField()
    payment_options=models.CharField(max_length=20)

   
# def __str__(self):
        # return self.customer







