from django.contrib import admin
from django.contrib import admin
from .models.client import Client
from .models.booking import Booking

# Register your models here.

admin.site.register(Client)
admin.site.register(Booking)