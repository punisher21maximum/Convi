# Generated by Django 3.0.5 on 2020-05-05 06:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_quespaper'),
    ]

    operations = [
        migrations.AddField(
            model_name='quespaper',
            name='exam_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
