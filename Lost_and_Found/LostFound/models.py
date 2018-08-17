import datetime
import importlib
from django.db import models
from .choices import *

# Create instance info*********************************************************

class Instance_info(models.Model):  
    instance_id = models.AutoField(primary_key=True, editable=False)
    instance_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

# Create reported item info****************************************************

class Item_info(models.Model):    
    item_name = models.CharField(max_length=255, blank=False)
    item_category = models.CharField(max_length=255, choices=Item_Category_Choices, blank=False)
    place = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)
    item_desc = models.TextField(blank=True)
    item_status = models.CharField(max_length=255, null=False)
    reported_spam = models.BooleanField(default=False)
    item_is_spam = models.BooleanField(default=False)

    class Meta:
        abstract = True

# Create Lost item model*******************************************************
 
class Lost(Item_info, Instance_info):

    def __init__(self, *args, **kwargs):
        self._meta.get_field('item_status').choices = Lost_Status_Choices
        self._meta.get_field('item_status').default = 'Nf'
        super(Lost,self).__init__(*args, **kwargs)
    
    class Meta:
        verbose_name = "Lost"
        verbose_name_plural = "Report Lost"
    
    
# Create Found item model******************************************************

class Found(Item_info, Instance_info):

    def __init__(self, *args, **kwargs):
        self._meta.get_field('item_status').choices = Found_Status_Choices
        self._meta.get_field('item_status').default = 'On'
        super(Found,self).__init__(*args, **kwargs)

    class Meta:
        verbose_name = "Found"
        verbose_name_plural = "Report Found"
 