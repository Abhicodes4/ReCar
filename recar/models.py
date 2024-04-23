from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name



class Cars(models.Model):
    name=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    year=models.CharField(max_length=30)
    km=models.CharField(max_length=30)
    ownership=models.CharField(max_length=30)
    transmission=models.CharField(max_length=30,null=True,blank=True)
    company=models.CharField(max_length=30,null=True,blank=True)
    image=models.ImageField(upload_to='profile_pic1',null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    us=models.ForeignKey(User,on_delete=models.CASCADE)
    
    

