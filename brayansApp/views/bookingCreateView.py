from rest_framework import status, views, generics
from rest_framework.response import Response
from brayansApp.models.booking import Booking
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from django.conf import settings

from brayansApp.serializers.bookingSerializer import BookingSerializer
from brayansApp.serializers.clientSerializer import ClientSerializer

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all() #modelo de booking
    serializer_class = BookingSerializer
    #permission_classes = (IsAuthenticated,) #se descomenta cuando termino de hacer pruebas

    def list(self, request):
        print("GET a todos los Booking")
        queryset = self.get_queryset()
        serializer = BookingSerializer(queryset, many=True) #queryset es para listar usr en BD
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("POST a Booking")
        print(request.data)

        usuarioData = request.data.pop('usuario') #el metodo pop recupera la info de la llave usuario
        serializerU = ClientSerializer(data=usuarioData)
        serializerU.is_valid(raise_exception=True) #para verificar que la data es valida
        usuario = serializerU.save()
        
        enfData = request.data
        enfData.update({"usuario":usuario.id})
        serializerEnf = BookingSerializer(data=enfData)      
        serializerEnf.is_valid(raise_exception=True)
        serializerEnf.save()
        return Response(status=status.HTTP_201_CREATED)
        
        '''tokenData = {
                       "username": request.data["username"],
                       "password": request.data["password"]
                       }
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)'''
 
'''
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)'''

class BookingRetrieveUpddateView(generics.RetrieveUpdateAPIView): #obtener, actualizar, borrar
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = 'id' #campo con el que se realiza la busqueda de los objetos, el ID de la PK
    lookup_url_kwarg = 'pk' #nombre dado en la URL al argumento
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a Booking")
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTORIZED)
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print("PUT a Booking")
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTORIZED)
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        print("DELETE a Booking")
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTORIZED)
        return super().delete(request, *args, **kwargs)