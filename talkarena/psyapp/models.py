from django.db import models

# Create your models here.
class pregdb(models.Model):
    pname=models.CharField(max_length=30)
    pmail=models.EmailField()
    pqual=models.CharField(max_length=30,default='')
    pexp=models.IntegerField(default=0)
    pgen=models.CharField(max_length=30,default='')
    pprf=models.ImageField(upload_to='pregimgs',default='null.jpg')
    ppsw=models.TextField()
    status=models.IntegerField(default=0)
   
    