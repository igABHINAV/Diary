from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    username=models.CharField(max_length=200,blank=True,null=True)
    title = models.CharField(max_length=1000 , blank=True , null=True)
    message=models.CharField(max_length=100000,null=True,blank=True,default="")
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title