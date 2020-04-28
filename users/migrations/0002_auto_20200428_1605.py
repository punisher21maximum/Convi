# Generated by Django 3.0.5 on 2020-04-28 16:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fname',
            field=models.CharField(blank='True', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='lname',
            field=models.CharField(blank='True', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank='True', max_length=10, validators=[django.core.validators.RegexValidator(message='Enter valid phone number. Ensure 10 digit number starting with 9, 8, 7, or 6', regex='^[9876]\\d{9}$')]),
        ),
    ]
