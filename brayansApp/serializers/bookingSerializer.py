from brayansApp.models.booking import Booking
from rest_framework import serializers

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['bookingdate', 'people']