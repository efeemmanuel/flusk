from django.db import models

# Create your models here.


class beginners_class(models.Model):
    videofile= models.FileField(upload_to='beginners_video', null=True, verbose_name="")
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=60)
    tutor = models.CharField(max_length=10, null=True,)
    minutes = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    

class advance_class(models.Model):
    videofile= models.FileField(upload_to='beginners_video', null=True, verbose_name="")
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=60)
    tutor = models.CharField(max_length=10, null=True,)
    minutes = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)  # Adjust max_length as needed
    message = models.TextField(max_length=300)