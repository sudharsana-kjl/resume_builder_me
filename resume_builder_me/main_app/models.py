from __future__ import unicode_literals
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
	#user = models.OneToOneField(User, on_delete=models.CASCADE)
	#resume_file = models.FileField(upload_to = 'books')

	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)

	DEPT_CHOICES = (
		('CSE', 'CSE'),
		('ECE', 'ECE'),
		('EEE', 'EEE'),
		('MECH', 'MECH'),
		('ICE', 'ICE'),
		('CHEM', 'CHEM'),
		('PROD', 'PROD'),
		('CIVIL', 'CIVIL'),
		('META', 'META'),
	)
	
	user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
	name = models.CharField(max_length = 200)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	Nationality = models.CharField(max_length=200)
	address = models.TextField()
	email = models.EmailField()
	father_name = models.CharField(max_length=200)
	date_of_birth = models.DateField(default=timezone.now())
	languages = models.CharField(max_length = 200)
	branch = models.CharField(max_length=5, choices=DEPT_CHOICES)
	cgpa = models.CharField(max_length=10)
	programming_languages = models.CharField(max_length=200)
	operating_systems = models.CharField(max_length=200)
	packages = models.CharField(max_length=100)
	acad_details = models.TextField()
	sports_details = models.TextField()
	other_details = models.TextField()
	position_of_resp = models.TextField()
	Xth_class_board = models.CharField(max_length=10)
	Xth_school_name = models.CharField(max_length=200)
	Xth_board_mark = models.CharField(max_length=20)
	XIIth_class_board = models.CharField(max_length=10)
	XIIth_school_name = models.CharField(max_length=200)
	XIIth_board_mark = models.CharField(max_length=20)
	
	def __str__(self):
		return self.name
# Create your models here.

class Project(models.Model):
	title = models.CharField(max_length = 200, blank=True,null=True)
	detail = models.TextField(blank=True,null=True)
	start_date = models.DateField(default=timezone.now(),blank=True,null=True)
	end_date = models.DateField(default=timezone.now(),blank=True,null=True)
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

