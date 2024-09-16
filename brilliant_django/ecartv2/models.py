from django.db import models

# Create your models here.
class EmployeeModelV2(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=100)
    email = models.EmailField()
    