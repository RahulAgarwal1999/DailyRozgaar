from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    number = models.IntegerField(null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address = models.TextField(null=True)
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
