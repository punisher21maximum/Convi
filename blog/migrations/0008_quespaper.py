# Generated by Django 3.0.5 on 2020-05-05 06:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_auto_20200425_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuesPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(blank=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('starred', models.BooleanField(default=False)),
                ('academic_year', models.CharField(choices=[('FY', 'I'), ('SY', 'II'), ('TY', 'III'), ('BE', 'IV')], default='I', max_length=100)),
                ('branch', models.CharField(choices=[('CS', 'CS'), ('Mech', 'Mech'), ('ENTC', 'ENTC'), ('IT', 'IT'), ('CHEM', 'CHEM'), ('ETX', 'ETX'), ('Civil', 'Civil'), ('FY', 'FY')], default='CS', max_length=100)),
                ('sub', models.CharField(choices=[('NO SUBJECT', 'NO SUBJECT'), ('DSF', 'Data Structures And Files'), ('DSGT', 'Data Structures and Graph Theory'), ('AM2', 'Applied Mathematcs'), ('AM1', 'Applied Mechanics'), ('EI', 'Engineering Informatics'), ('DBMS', 'DBMS'), ('SYSTEM ENGG', 'SYSTEM ENGG'), ('MATHS', 'MATHS'), ('PSYCHO', 'PSYCHO'), ('MATERIAL ENGG', 'MATERIAL ENGG'), ('PYTHON', 'PYTHON'), ('CPP', 'CPP'), ('EEE', 'EEE'), ('None', 'none')], default='NO SUBJECT', max_length=100)),
                ('sem_exam', models.CharField(choices=[('ISE1', 'ISE1'), ('ISE2', 'ISE2'), ('MSE', 'MSE'), ('ESE', 'ESE'), ('ISE', 'ISE')], default='ESE', max_length=100)),
                ('total_marks', models.PositiveIntegerField(blank=True, default=100)),
                ('exam_type', models.CharField(choices=[('Regular', 'Regular'), ('Re-exam', 'Re-exam')], default='Rgular', max_length=100)),
                ('fileMy', models.FileField(blank=True, upload_to='Ques_papers')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]