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


class Reporter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    # This is creating a fk to a reporter 
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)


class StudentName(models.Model):
    name = models.CharField(max_length=255)


class Project(models.Model):
    project_name = models.CharField(max_length=255)
    due_date = models.DateField()
    student = models.ManyToManyField(StudentName, through='ProjectStudentRelationship')

class ProjectStudentRelationship(models.Model):
    student = models.ForeignKey(StudentName, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)