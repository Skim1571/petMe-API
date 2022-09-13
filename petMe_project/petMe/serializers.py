from rest_framework import serializers
from .models import Species,Pet
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer

class SpeciesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Species
    fields = ('id', 'name','image_url')

class PetSerializer(WritableNestedModelSerializer):
  species = SpeciesSerializer(
    read_only=False,
    required=False
  )

  class Meta:
    model = Pet
    fields = ('id', 'name', 'age','birth_date','hunger','affection','health','last_play_time','last_fed_time','image_url','species', 'user')


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
  pets = PetSerializer(
  many=True,
  read_only=False
  )
  class Meta:
    model = User
    fields = ("id", "username", "password", "email","pets")

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)

    # Add custom claims
    token['username'] = user.username
    token['email'] = user.email
    # ...
    return token