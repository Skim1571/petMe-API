from django.db import models

# Create your models here.
class User(models.Model):
  username = models.CharField(max_length=20)
  email = models.CharField(max_length=50)
  password = models.CharField(max_length=20)

  def __str__(self):
    return self.username

class Species(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Pet(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets', null=True)
  species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name='pets', unique=True, default=1)
  name = models.CharField(max_length=20)
  age = models.IntegerField(default=0)
  birth_date = models.DateField(auto_now_add=True)
  hunger = models.IntegerField(default=50)
  affection = models.IntegerField(default=50)
  health = models.IntegerField(default=100)
  last_play_time = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name