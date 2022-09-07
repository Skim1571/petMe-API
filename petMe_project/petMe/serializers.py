from rest_framework import serializers
from .models import User,Species,Pet



class SpeciesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Species
    fields = ('id', 'name',)

class PetSerializer(serializers.ModelSerializer):
  species = SpeciesSerializer(
    read_only=True
  )
  class Meta:
    model = Pet
    fields = ('id', 'name', 'age','birth_date','hunger','affection','health','last_play_time','image_url','species')

class UserSerializer(serializers.ModelSerializer):
  pets = PetSerializer(
    many=True,
    read_only=True

  )
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'pets')