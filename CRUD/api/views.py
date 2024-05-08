from .serializers import Student_serializer
from .models import Student
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.

class List_Create_api(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_serializer

    
class Retrieve_Update_Delete_api(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_serializer



    
