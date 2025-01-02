from django.db import models

# Create your models here.
class atregdb(models.Model):
    atname=models.CharField(max_length=30)
    atmail=models.EmailField()
    atprf=models.ImageField(upload_to='atregimgs',default='null.jpg')
    atpsw=models.TextField()
    status=models.IntegerField(default=0)