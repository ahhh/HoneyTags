from django.db import models

class Tag(models.Model):
	campaign = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
	key = models.CharField(max_length=200)
	type = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class Callbacks(models.Model):
	tag = models.ForeignKey(Tag)
	date = models.DateTimeField('date called back')
	ip = models.CharField(max_length=20)
	ua = models.CharField(max_length=200)
	
