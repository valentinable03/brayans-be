from brayansApp.models import booking
from brayansApp.models import client
from brayansApp.models.booking import Booking
from brayansApp.models.client import Client
from rest_framework import serializers

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','bookingdate', 'people','usuario']

'''    def create(self, validated_data):
        
        bookingInstance = Booking.objects.create(**validated_data)
        
        return bookingInstance

    def to_representation(self, obj):
        #booking = Booking.objects.get(id=obj.id)
       
        return {
                    #'id': booking.id,
                    'id': client.id,
                    'bookingdata': booking.bookingdate,
                    'poeple': booking.people,
        }'''