from rest_framework import serializers
from .models import User,Species,Pet

class UserSerializer(serializers.HyperlinkedModelSerializer):
  pets = serializers.HyperlinkedRelatedField(
    view_name='pet_detail',
    many=True,
    read_only=True
  )
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'pets',)

class SpeciesSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Species
    fields = ('id', 'name',)

class PetSerializer(serializers.HyperlinkedModelSerializer):
  user = serializers.HyperlinkedRelatedField(
    view_name='user_detail',
    read_only=True
  )
  species = serializers.HyperlinkedRelatedField(
    view_name='species_detail',
    read_only=True
  )
  class Meta:
    model = Pet
    fields = ('id', 'name', 'age','birth_date','hunger','affection','health','last_play_time','species','user',)