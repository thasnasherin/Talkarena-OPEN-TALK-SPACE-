from django.db import models
from psyapp.models import *
from authapp.models import * 
# Create your models here.
class regdb(models.Model):
    uname=models.CharField(max_length=70)
    umail=models.EmailField()
    uprf=models.ImageField(upload_to='regimgs',default='null.jpg')
    upsw=models.TextField()

class contdb(models.Model):
    cname=models.CharField(max_length=30)
    cmail=models.EmailField()
    csub=models.CharField(max_length=100, default='none')
    cmsg=models.TextField()

class psyapn(models.Model):
    uid=models.ForeignKey(regdb,on_delete=models.CASCADE)
    pid=models.ForeignKey(pregdb,on_delete=models.CASCADE)
    num=models.IntegerField()
    sub=models.CharField(max_length=40)
    dte=models.DateField()
    tme=models.TimeField()
    status=models.IntegerField(default=0)
    rid=models.CharField(max_length=1000, null=True)

class atapn(models.Model):
    uid=models.ForeignKey(regdb,on_delete=models.CASCADE)
    aid=models.ForeignKey(atregdb,on_delete=models.CASCADE)
    num=models.IntegerField()
    sub=models.CharField(max_length=40)
    dte=models.DateField()
    tme=models.TimeField()
    status=models.IntegerField(default=0)

class topic(models.Model):
    uid=models.ForeignKey(regdb,on_delete=models.CASCADE)
    top=models.CharField(max_length=50)

class reply(models.Model):
    did=models.ForeignKey(topic,on_delete=models.CASCADE)
    rep=models.CharField(max_length=1000)
