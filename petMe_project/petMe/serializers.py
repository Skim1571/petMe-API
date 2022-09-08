from rest_framework import serializers
# from .models import User,Species,Pet
from django.contrib.auth import get_user_model


# class SpeciesSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Species
#     fields = ('id', 'name',)

# class PetSerializer(serializers.ModelSerializer):
#   species = SpeciesSerializer(
#     read_only=True
#   )
#   class Meta:
#     model = Pet
#     fields = ('id', 'name', 'age','birth_date','hunger','affection','health','last_play_time','image_url','species')

# class UserSerializer(serializers.ModelSerializer):
#   pets = PetSerializer(
#     many=True,
#     read_only=True
#   )
#   class Meta:
#     model = User
#     fields = ('id', 'username','email', 'pets')
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)
  def create(self, validated_data):
    """
    Create and return a new User instance, given the validated data.
    """
    # make sure to user create_user method and not create
    # the later will not know how to hash the password properly
    user = User.objects.create_user(
      username=validated_data["username"],
      password=validated_data["password"],
      email=validated_data["email"],
      )
    return user
  class Meta:
    model = User
    fields = ("id", "username", "password", "email")

