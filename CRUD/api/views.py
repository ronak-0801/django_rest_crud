from .serializers import Student_serializer
from .models import Student
from rest_framework import viewsets

# Create your views here.

class Crudapi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Student_serializer

    
class Read_only_api(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Student_serializer



    
