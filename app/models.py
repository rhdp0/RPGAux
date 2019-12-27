from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class main(models.Model):
    text = models.TextField()

class Users(models.Model):
    name = models.CharField(max_length=20, null=False)
    username = models.CharField(max_length=16, null=False)
    email = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=16, null=False)

    def __str__(self):
        return self.name
# Create your models here.
