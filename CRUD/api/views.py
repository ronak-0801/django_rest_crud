
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Student_serializer
from .models import Student
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin

# Create your views here.

class List_Create_api(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = Student_serializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs) 
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs) 
    
class Retrieve_Update_Delete_api(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = Student_serializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs) 

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs) 

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs) 
    


    
