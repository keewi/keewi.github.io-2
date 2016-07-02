from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class University(models.Model):
	# identifying infromation
	long_name = models.CharField(max_length=50)
	short_name = models.CharField(max_length=20)

	# school profile 
	email_end = models.CharField(max_length=20)

class Student(models.Model):
	# identifying information
	user_id = models.CharField(max_length=200)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	
	# school profile information
	university_id = models.ForeignKey(University, on_delete=models.CASCADE)
	is_mentor = models.BooleanField(default=False)
	grad_year = models.IntegerField()

	# program interest information
	is_avail = models.IntegerField(default=2)
	rel_interest = models.CharField(max_length=100)

	# metadata
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user_id