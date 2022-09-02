from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer, SpeciesSerializer,PetSerializer
from .models import User,Species,Pet

# Create your views here.
class UserList(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
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