
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Student_serializer
from .models import Student

# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            st = Student.objects.get(pk=pk)
            serializer = Student_serializer(st)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        st = Student.objects.all()
        serializer = Student_serializer(st,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK) 
    
    if request.method == 'POST':
        serializer = Student_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        st = Student.objects.get(pk=pk)
        serializer = Student_serializer(st, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( {'msg':'data updated'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        st = Student.objects.get(pk=pk)
        serializer = Student_serializer(st, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response( {'msg':'data updated'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        st = Student.objects.get(pk=pk)
        st.delete()
        return Response( {'msg':'data deleted'},status=status.HTTP_200_OK)

    
