from django.db import models

# Create your models here.
class Gallery(models.Model):
	image = models.ImageField(upload_to='gallery/')
	heading = models.CharField(max_length=70)
	description = models.TextField()
	time = models.DateTimeField(auto_now_add=True)
class Blog(models.Model):
	image=models.ImageField()
	description=models.CharField(max_length=400)
	time = models.DateTimeField(auto_now_add=True)