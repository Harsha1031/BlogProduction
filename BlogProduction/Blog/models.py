from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserData(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)


class PosModel(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text=models.TextField(max_length=500)


class CommentModel(models.Model):
    post= models.ForeignKey(PosModel,on_delete=models.CASCADE,primary_key=True)
    writer = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
