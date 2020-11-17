from django.db import models
from datetime import datetime,date
# from django.forms import ModelForm


# Create your models here.

class Computer(models.Model):
    computer_name = models.CharField(max_length=30,blank=True)
    IP_address = models.CharField(max_length=30,blank=True)
    MAC_address = models.CharField(max_length=30,blank=True)
    user_name = models.CharField(max_length=30,blank=True)
    location = models.CharField(max_length=30,blank=True)
    purchase_date = models.DateField('Purchase Date(dd/mm/yyyy)',auto_now_add=False,auto_now=False,blank=True)
    timestamp = models.DateField(auto_now=False,auto_now_add=True,blank=True)

    def __unicode__(self):
        return self.IP_address +''+self.computer_name