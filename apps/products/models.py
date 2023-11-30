from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=35)
    price = models.DecimalField(max_digits=10, decimal_places=2)
