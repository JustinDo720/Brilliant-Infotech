# Generated by Django 5.1.1 on 2024-09-11 00:38

import ecart.fileChecker
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecart', '0003_studentmodel_image_alter_studentmodel_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='file',
            field=ecart.fileChecker.ContentTypeRestrictedFileField(null=True, upload_to='files/'),
        ),
    ]
