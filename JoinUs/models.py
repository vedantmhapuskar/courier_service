import email
from django.db import models

# Create your models here.
class jobapp(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phonenumber = models.IntegerField()
    city = models.CharField(max_length=100)
    empstatus = models.CharField(max_length=100)
    resume = models.FileField(upload_to='files')
    
    def __str__(self):
        return self.firstname