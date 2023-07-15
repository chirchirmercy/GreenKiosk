from django.db import models

# Create your models here.


class Cart (models.Model):
    name = models.CharField(max_length=32)
    quantity = models.PositiveIntegerField()
    user_id = models.CharField(max_length=24)
    total_items = models.FloatField()

    def __str__(self):
        return self.name





