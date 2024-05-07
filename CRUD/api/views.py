
from .models import Student

from rest_framework.parsers import JSONParser

from django.http import JsonResponse
from .serializers import Student_serializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        python_data = JSONParser().parse(request)
        id = python_data.get('id', None)
        if id is not None:
            st = Student.objects.get(id=id)
            serializer = Student_serializer(st)
            return JsonResponse(serializer.data,safe=False)
        st = Student.objects.all()
        serializer = Student_serializer(st,many=True)
        return JsonResponse(serializer.data,safe=False) 
    
    if request.method == 'POST':
        python_data = JSONParser().parse(request)
        serializer = Student_serializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg':'data created'}
            return JsonResponse(msg,safe=False)
        return JsonResponse(serializer.errors)
    
    if request.method == 'PUT':
        python_data = JSONParser().parse(request)
        id = python_data.get('id')
        st = Student.objects.get(id=id)
        serializer = Student_serializer(st, data=python_data, partial = True)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg':'data updated'}
            return JsonResponse(msg,safe=False)
        return JsonResponse(serializer.errors)
    
    if request.method == 'DELETE':
        python_data = JSONParser().parse(request)
        id=python_data.get('id')
        st = Student.objects.get(id = id)
        st.delete()
        msg = {'msg':'data deleted'}
        return JsonResponse(msg,safe=False)

    
