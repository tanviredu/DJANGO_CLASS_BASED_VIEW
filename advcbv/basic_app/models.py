from django.db import models
from django.urls import reverse
## this is a school administration websirte

class School(models.Model):
	name 		= models.CharField(max_length=200)
	printciple  = models.CharField(max_length=256)
	location    = models.CharField(max_length=200)


	def __str__(self):
		return self.name 


	def get_absolute_url(self):
		return reverse('basic_app:schoolDetail',kwargs={'pk':self.pk})


class Student(models.Model):
	name        = models.CharField(max_length=200)
	age         = models.PositiveIntegerField()
	school      = models.ForeignKey(School,related_name="students",on_delete=models.CASCADE)


	def __str__(self):
		return self.name  


	def get_absolute_url(self):
		return reverse('basic_app:studentList')	


