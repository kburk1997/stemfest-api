from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Activity(models.Model):
  name=models.CharField(max_length=30)
  presenter=models.CharField(max_length=100)
  grades=models.CharField(max_length=10)
  description=models.TextField()

  def __str__(self):
    return self.name