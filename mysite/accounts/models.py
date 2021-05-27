from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserDetails(models.Model):
    number = models.IntegerField(null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    addressl1 = models.TextField(null=True)
    addressl2 = models.TextField(null=True)
    city = models.TextField(null=True)
    state = models.TextField(null=True)
    code = models.IntegerField(null=True)
    def __str__(self):
        return self.user_id.username


class WorkerDetails(models.Model):
    number = models.IntegerField(null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address = models.TextField(null=True)
    cardtype = models.CharField(null=True,max_length=100)
    cardnumber = models.CharField(null=True,max_length=100)
    job = models.CharField(null=True,max_length=100)
    status = models.CharField(null=True,blank=True,max_length=50)
    def __str__(self):
        return self.user_id.username


class Service(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    service_id=models.CharField(null=False,max_length=20,default='DR000000')
    service = models.CharField(max_length=100,null=True)
    adetails = models.TextField(null=True)
    time  = models.CharField(max_length=50,null=True)
    number = models.IntegerField(null=True)
    email = models.CharField(null=True,max_length=100)
    addressl1 = models.TextField(null=True)
    addressl2 = models.TextField(null=True)
    city = models.TextField(null=True)
    state = models.TextField(null=True)
    code = models.IntegerField(null=True)
    list_date = models.DateTimeField(default=timezone.now,blank=True)

    def __str__(self):
        return self.user_id.username

class ServiceHistory(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    service_id=models.CharField(null=False,max_length=20,default='DR000000')
    service = models.CharField(max_length=100,null=True)
    adetails = models.TextField(null=True)
    time  = models.CharField(max_length=50,null=True)
    addressl1 = models.TextField(null=True)
    addressl2 = models.TextField(null=True)
    city = models.TextField(null=True)
    state = models.TextField(null=True)
    code = models.IntegerField(null=True)
    list_date = models.DateTimeField(default=timezone.now,blank=True)

    def __str__(self):
        return self.user_id.username
