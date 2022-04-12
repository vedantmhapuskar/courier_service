from random import choice, choices
from django.db import models
import random
from gfg import settings
from django.contrib.auth.models import User

def random_string():
    return str(random.randint(1000000000, 9999999999))

A_choice = (('Order Pending','-'),('Order Accepted','Order Accepted'))
B_choice = (('-','-'),('Package Picked Up','Package Picked Up'))
C_choice = (('-','-'),('Package Left For Drop City','Package Left For Drop City'))
D_choice = (('-','-'),('Package Reached Drop City','Package Reached Drop City'))
E_choice = (('-','-'),('Package Delivered Successfully ','Package Delivered Successfully '))



class packagedetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, )
    track_id = models.TextField(default= random_string , blank=True)
    weight = models.IntegerField()
    slct1 = models.CharField(max_length=100)
    slct2 = models.CharField(max_length=100)
    city1 = models.CharField(max_length=100)
    pincode1 = models.IntegerField()
    state1 = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    city2 = models.CharField(max_length=100)
    pincode2 = models.IntegerField()
    state2 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    accept = models.CharField(max_length=100 , choices=A_choice, blank=True ,  default=A_choice[0][0])
    pickup = models.CharField(max_length=100 ,choices=B_choice, blank=True ,  default=B_choice[0][0])
    left = models.CharField(max_length=100 , choices=C_choice, blank=True ,  default=C_choice[0][0])
    reach = models.CharField(max_length=100 ,choices=D_choice, blank=True ,  default=D_choice[0][0])
    shipped = models.CharField(max_length=100 , choices=E_choice, blank=True ,  default=E_choice[0][0])
    




        
