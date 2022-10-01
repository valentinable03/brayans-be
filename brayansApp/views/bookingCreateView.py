from rest_framework import status, views
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from brayansApp.serializers.bookingSerializer import BookingSerializer

class BookingCreateView(views.APIView):

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)