from django.db import models
import datetime

# Create your models here.
class ljud(models.Model):
    audio = models.URLField()
    pub_date =  models.DateField()
    audio_name = models.CharField(max_length=140)
    
class likes(models.Model):
    ljud = models.ForeignKey(ljud)
    likes = models.IntegerField()
    

