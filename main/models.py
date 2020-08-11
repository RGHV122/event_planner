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

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head0 = models.CharField(max_length=500, default="")
    chead0 = models.CharField(max_length=5000, default="")
    head1 = models.CharField(max_length=500, default="")
    chead1 = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.title