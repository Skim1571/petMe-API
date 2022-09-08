from django.urls import path
from .views import CreateUserView
from rest_framework.routers import DefaultRouter

urlpatterns = [
  # path('users/', views.UserList.as_view(), name='user_list'),
  # path('species/', views.SpeciesList.as_view(), name='species_list'),
  # path('pets/', views.PetList.as_view(), name='pet_list'),
  # path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
  # path('species/<int:pk>', views.SpeciesDetail.as_view(), name='species_detail'),
  # path('pets/<int:pk>', views.PetDetail.as_view(), name='pet_detail'),
  path("signup/", CreateUserView.as_view(), name='create_user')
]