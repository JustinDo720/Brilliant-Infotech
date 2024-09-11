from django.db import models
from .fileChecker import ContentTypeRestrictedFileField

# Create your models here.
class Project(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_qty = models.IntegerField()


# Student Model used in forms.py
class StudentModel(models.Model):
    name = models.CharField(max_length=60)
    marks = models.IntegerField()
    document = ContentTypeRestrictedFileField(null=True, upload_to='files/', content_types=['application/vnd.openxmlformats-officedocument.wordprocessingml.document', ],max_upload_size=500000)
    image = models.ImageField(null=True, upload_to='upload/')

