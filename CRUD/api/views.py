from .serializers import Student_serializer
from .models import Student
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
# Create your views here.

class Crudapi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Student_serializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle,UserRateThrottle]
    

