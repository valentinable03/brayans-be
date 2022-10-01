from django.db import models
from .client import Client

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Client, related_name='booking', on_delete=models.CASCADE)
    bookingdate = models.DateTimeField()
    people = models.IntegerField(default=0)
    