from django.db import models

# Create your models here.
class User(models.Model):
  username = models.CharField(max_length=20)
  email = models.CharField(max_length=50)
  password = models.CharField(max_length=20)

  def __str__(self):
    return self.name

class Species(models.Model):
  species = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Pet(models.Model):
  name = models.CharField(max_length=20)
  age = models.IntegerField()
  birth_date = models.DateField()
  hunger = models.IntegerField()
  affection = models.IntegerField()
  health = models.IntegerField()
  last_play_time = models.DateTimeField()

  def __str__(self):
    return self.name