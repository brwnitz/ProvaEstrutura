from django.db import models
from django.utils import timezone

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=0)
    name = models.TextField(max_length=40,default='Placeholder')
    sales= models.IntegerField(default=0)
    perishable = models.BooleanField(default=True)
    expire_date = models.DateTimeField(default=None,null=True)
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)


