from django.db import models

# Create your models here.z

class Schedule(models.Model):

  name = models.CharField(max_length=50)
  date = models.DateField()
  time = models.CharField(max_length=50)

  def __str__(self):
      return f'{self.name}: {self.date}'

class Thisday(models.Model):

  date = models.DateField()
  time7 = models.CharField(max_length=50)
  time8 = models.CharField(max_length=50)
  time9 = models.CharField(max_length=50)
  time10 = models.CharField(max_length=50)
  time11 = models.CharField(max_length=50)

  def __str__(self):
      return f'{self.name}: {self.date}'