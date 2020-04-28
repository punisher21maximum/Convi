from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_file = models.FileField(upload_to='blog_pdf',blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# #6 unit long ID 
# import string, random
# def id_generatot(size=6, chars=string.ascii_uppercase + string.digits):
# 	return ''.join(random.choice(chars) for i in range(size))
# def get_id():

from django import template
register = template.Library()
lenn = 100
class Common(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	desc = models.TextField(blank=True)
	date_posted = models.DateTimeField(default=timezone.now)
	starred = models.BooleanField(default=False)

	class Meta:
		abstract = True

	

class College(Common):
	Year_CHOICES=[('FY','I'),('SY','II'),('TY','III'),('BE','IV')]
	academic_year=models.CharField(max_length=lenn,choices=Year_CHOICES,default='I')
	Branch_CHOICES=[('CS','CS'),('Mech','Mech'),('ENTC','ENTC'),('IT','IT'),
	('CHEM','CHEM'),('ETX','ETX'),('Civil','Civil'),('FY','FY')]
	branch=models.CharField(max_length=lenn,choices=Branch_CHOICES,default='CS')
	Subject_CHOICES=[('NO SUBJECT','NO SUBJECT'),('DSF','Data Structures And Files'),('DSGT','Data Structures and Graph Theory'),('AM2','Applied Mathematcs'),
		('AM1','Applied Mechanics'),('EI','Engineering Informatics'),('DBMS','DBMS'),('SYSTEM ENGG','SYSTEM ENGG'),
		('MATHS','MATHS'),('PSYCHO','PSYCHO'),('MATERIAL ENGG','MATERIAL ENGG'),('PYTHON','PYTHON'),('CPP','CPP'),
		('EEE','EEE'),	('None','none')]	
	sub=models.CharField(max_length=lenn,choices=Subject_CHOICES,default='NO SUBJECT')
	#dependent forms
	# course_code = based on the subject, branch, year ,not taken from user

	class Meta:
		abstract = True

class Enotes(College):
	topic = models.CharField(max_length=100)
	unit = models.PositiveIntegerField(blank=True, default=1)
	Notes_author_CHOICES=[('teacher','Teacher'),('student','Student'),('other','Other')]
	notes_author = models.CharField(max_length=lenn,choices=Notes_author_CHOICES,default='Anonymous')
	author_name = models.CharField(max_length=100)
	fileMy = models.FileField(upload_to='blog_pdf',blank=True)

	def __str__(self):
		return self.topic

	def get_absolute_url(self):
		return reverse('enotes-detail', kwargs={'pk': self.pk})
    
	