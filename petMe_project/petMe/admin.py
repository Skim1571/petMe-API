from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Species,Pet
admin.site.register(Species)
admin.site.register(Pet)