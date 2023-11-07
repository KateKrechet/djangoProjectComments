from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

class Kino(models.Model):
    title = models.CharField(max_length=40)
    link = models.URLField()


class Comment(models.Model):
    name = models.CharField(max_length=20)
    body = models.TextField()
    timedata = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    like = models.IntegerField(default=0)
    kino = models.ForeignKey(Kino, on_delete=models.SET_NULL, null=True,blank=True)




