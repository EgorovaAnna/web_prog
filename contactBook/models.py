# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contact(models.Model):
	surname = models.CharField(max_length = 30)
	name = models.CharField(max_length = 30)
	patronymic = models.CharField(max_length = 30)
	gender = models.CharField(max_length = 1, default = 'N')
	birthday = models.DateField();
	job = models.ForeignKey('Job', on_delete=models.CASCADE)
	post = models.ForeignKey('Post', on_delete=models.CASCADE)
	telephone = models.CharField(max_length = 30)
	email = models.EmailField()
	street = models.ForeignKey('Street', on_delete=models.CASCADE)
	building = models.CharField(max_length = 5)
	apartment = models.PositiveSmallIntegerField()
	
class Job(models.Model):
	job = models.CharField(max_length = 30)
	def __str__(self):
		return self.job.encode('utf8')
	
class Post(models.Model):
	post = models.CharField(max_length = 30)
	def __str__(self):
		return self.post.encode('utf8')
	
class City(models.Model):
	city = models.CharField(max_length = 30)
	def __str__(self):
		return self.city.encode('utf8')
	
class Street(models.Model):
	street = models.CharField(max_length = 30)
	city = models.ForeignKey('City', on_delete=models.CASCADE)
	def __str__(self):
		return self.street.encode('utf8')