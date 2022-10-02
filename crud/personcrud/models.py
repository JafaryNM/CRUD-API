from django.db import models

# Create your models here.

class Person(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

    def __str__(self):
        return self.name
