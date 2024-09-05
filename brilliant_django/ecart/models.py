from django.db import models

# Create your models here.
class Project(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_qty = models.IntegerField()