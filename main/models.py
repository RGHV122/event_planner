from django.db import models

# Create your models here.
class Gallery(models.Model):
	image = models.ImageField(upload_to ='media/gallery/')
	description = models.CharField(max_length=100)
	time = models.DateTimeField(auto_now_add=True)
class Blog(models.Model):
	image=models.ImageField(upload_to='media/blog/')
	description=models.CharField(max_length=400)
	time = models.DateTimeField(auto_now_add=True)