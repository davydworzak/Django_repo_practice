from __future__ import unicode_literals

from django.db import models

class Movie(models.Model):
	title=models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)

class Actor(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
