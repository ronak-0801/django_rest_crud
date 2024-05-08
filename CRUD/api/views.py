from .serializers import Student_serializer
from .models import Student
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class Crudapi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Student_serializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    

