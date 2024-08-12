from django.db import models

# Create your models here.
class bookinfo(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    isbn=models.CharField(max_length=20)
    publisher=models.CharField(max_length=20)