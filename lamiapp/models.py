from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class main_page_pic(models.Model):
    image1=models.ImageField(upload_to='blog_image')
    image2=models.ImageField(upload_to='blog_image')
    image3=models.ImageField(upload_to='blog_image')
    image4=models.ImageField(upload_to='blog_image')
    image5=models.ImageField(upload_to='blog_image')
    image6=models.ImageField(upload_to='blog_image')
    image7=models.ImageField(upload_to='blog_image')
    image8=models.ImageField(upload_to='blog_image')
    image9=models.ImageField(upload_to='blog_image')
    image10=models.ImageField(upload_to='blog_image')
    image11=models.ImageField(upload_to='blog_image')

    def _str_(self):
        return self.image

    class Meta:
        ordering=['-id']
class potraits(models.Model):
    image1=models.ImageField(upload_to='blog_image')
    image2=models.ImageField(upload_to='blog_image')
    image3=models.ImageField(upload_to='blog_image')
    image4=models.ImageField(upload_to='blog_image')
    image5=models.ImageField(upload_to='blog_image')
    image6=models.ImageField(upload_to='blog_image')
    image7=models.ImageField(upload_to='blog_image')
    image8=models.ImageField(upload_to='blog_image')
    image9=models.ImageField(upload_to='blog_image')
    image10=models.ImageField(upload_to='blog_image')
    image11=models.ImageField(upload_to='blog_image')

    def _str_(self):
        return self.image

    class Meta:
        ordering=['-id']
class event_pic(models.Model):
    image1=models.ImageField(upload_to='blog_image')
    image2=models.ImageField(upload_to='blog_image')
    image3=models.ImageField(upload_to='blog_image')
    image4=models.ImageField(upload_to='blog_image')
    image5=models.ImageField(upload_to='blog_image')
    image6=models.ImageField(upload_to='blog_image')
    image7=models.ImageField(upload_to='blog_image')
    image8=models.ImageField(upload_to='blog_image')
    image9=models.ImageField(upload_to='blog_image')
    image10=models.ImageField(upload_to='blog_image')
    image11=models.ImageField(upload_to='blog_image')

    def _str_(self):
        return self.image

    class Meta:
        ordering=['-id']

class projects(models.Model):
    title=models.CharField(max_length=200)
    
    body=models.TextField(blank=True)
   
    date_created=models.DateTimeField(auto_now_add=True)
    image1=models.ImageField(upload_to='blog_image')
    image2=models.ImageField(upload_to='blog_image')
    image3=models.ImageField(upload_to='blog_image')
    image4=models.ImageField(upload_to='blog_image')
    image5=models.ImageField(upload_to='blog_image')
    image6=models.ImageField(upload_to='blog_image')
    image7=models.ImageField(upload_to='blog_image')
    image8=models.ImageField(upload_to='blog_image')
    image9=models.ImageField(upload_to='blog_image')
    image10=models.ImageField(upload_to='blog_image')
    image11=models.ImageField(upload_to='blog_image')

    def _str_(self):
        return self.title
    
    class Meta:
        ordering=['-id']





