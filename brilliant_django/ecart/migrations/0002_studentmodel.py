# Generated by Django 5.1.1 on 2024-09-10 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('marks', models.IntegerField()),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
