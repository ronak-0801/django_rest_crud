
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Student_serializer
from .models import Student

# Create your views here.

class Student_api(APIView):
    def get(self, request,pk = None, format=None):
        if pk is not None:
            st = Student.objects.get(pk=pk)
            serializer = Student_serializer(st)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        st = Student.objects.all()
        serializer = Student_serializer(st,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK) 
    
    def post(self,request,format=None):
        serializer = Student_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request,pk = None, format=None):
        st = Student.objects.get(pk=pk)
        serializer = Student_serializer(st, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( {'msg':'data updated'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def patch(self, request,pk = None, format=None):
        st = Student.objects.get(pk=pk)
        serializer = Student_serializer(st, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response( {'msg':'data updated'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request,pk = None, format=None):
        st = Student.objects.get(pk=pk)
        st.delete()
        return Response( {'msg':'data deleted'},status=status.HTTP_200_OK)

    
