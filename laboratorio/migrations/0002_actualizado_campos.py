# Generated by Django 5.1.1 on 2024-11-05 23:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='directorgeneral',
            name='especialidad',
            field=models.CharField(default='Químico farmaceutico', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='ciudad',
            field=models.CharField(default='Santiago', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='pais',
            field=models.CharField(default='Chile', max_length=50),
            preserve_default=False,
        ),
    ]
