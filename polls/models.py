from django.db import models
class BooK(models.Model):
  name=models.CharField(max_length=200)
  author=models.CharField(max_length=100)
  pub_house=models.CharField(max_length=200)
  pub_date=models.DateTimeField('date published')

# Create your models here.
