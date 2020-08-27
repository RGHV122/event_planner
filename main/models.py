from django.db import models
from datetime import date
# Create your models here.
class Gallery(models.Model):
	image = models.ImageField(upload_to='gallery/')
	heading = models.CharField(max_length=70)
	time = models.DateTimeField(auto_now=True)

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,default="")
    blog_heading = models.CharField(max_length=100, default="")
    blog_description = models.CharField(max_length=5000, default="")
    blogpost = models.TextField(default="")
    pub_date = models.DateField(default =date.today)
    thumbnail = models.ImageField(upload_to='blog/images',default="")
    def __str__(self):
        return self.title
class ContactFormModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    event_detail = models.TextField()
