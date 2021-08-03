# from _typeshed import Self
from django.db import models


# Create your models here.
class Users(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    def __repr__(self):
        return f"<user object : {self.firstname}, {self.lastname}, {self.email}, {self.age}, ({self.id})>"