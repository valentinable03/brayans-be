from rest_framework import serializers
from brayansApp.models.client import Client
from brayansApp.models.booking import Booking
from brayansApp.serializers.bookingSerializer import BookingSerializer

class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = ['id', 'username', 'password', 'name', 'lastname', 'address', 'phone', 'email']

'''    def create(self, validated_data):
        
        clientInstance = Client.objects.create(**validated_data)
        
        return clientInstance

    def to_representation(self, obj):
        client = Client.objects.get(id=obj.id)
       
        return {
                    'id': client.id,
                    'username': client.username,
                    'name': client.name,
                    'lastname': client.lastname,
                    'address': client.address,
                    'phone': client.phone,
                    'email': client.email,
                    
}'''