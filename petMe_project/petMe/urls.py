from django.urls import path
from .views import CreateUserView, SpeciesList, SpeciesDetail, PetList, PetDetail, UserList, UserDetail, MyTokenObtainPairView
from rest_framework.routers import DefaultRouter

urlpatterns = [
  path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('users/', UserList.as_view(), name='user_list'),
  path('species/', SpeciesList.as_view(), name='species_list'),
  path('pets/', PetList.as_view(), name='pet_list'),
  path('users/<int:pk>', UserDetail.as_view(), name='user_detail'),
  path('species/<int:pk>', SpeciesDetail.as_view(), name='species_detail'),
  path('pets/<int:pk>', PetDetail.as_view(), name='pet_detail'),
  path("signup/", CreateUserView.as_view(), name='create_user')
]