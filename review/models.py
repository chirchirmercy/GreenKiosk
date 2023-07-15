from django.db import models

# Create your models here.

class Review (models.Model):
    message = models.TextField()
    sender = models.CharField(max_length=40)
    products =models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.sender









