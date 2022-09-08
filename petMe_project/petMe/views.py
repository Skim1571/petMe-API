from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer, PetSerializer, SpeciesSerializer
from .models import Species,Pet
from rest_framework import permissions
from django.contrib.auth import get_user_model

class CreateUserView(CreateAPIView):
  model = get_user_model()
  permission_classes = [
    permissions.AllowAny,  # Unauthenticated users must be able to sign up
  ]
  serializer_class = UserSerializer

# Create your views here.
class UserList(generics.ListCreateAPIView):
  queryset = get_user_model()
  serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = get_user_model()
  serializer_class = UserSerializer

class SpeciesList(generics.ListCreateAPIView):
  queryset = Species.objects.all()
  serializer_class = SpeciesSerializer

class SpeciesDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Species.objects.all()
  serializer_class = SpeciesSerializer

class PetList(generics.ListCreateAPIView):
  queryset = Pet.objects.all()
  serializer_class = PetSerializer

class PetDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Pet.objects.all()
  serializer_class = PetSerializer

