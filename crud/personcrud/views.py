from django.shortcuts import render
from .serializer import PersonSerializer
from .models import Person
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class PersonDetail(APIView):

    def get(self,request):
        
        ###### Return All Person In Database ##

        person_objects=Person.objects.all()
        person_object_serializers=PersonSerializer(person_objects, many=True)
        return Response(person_object_serializers.data)

    def post(self,request):
        serialized_object=PersonSerializer(data=request.data)
        if serialized_object.is_valid():
            serialized_object.save()
            return Response(200)

        return Response(serialized_object.errors)
    
class PersonUpdate(APIView):
   def post(self,request, pk):
    try:
       personal_object=Person.objects.get(pk=pk)
    except:
        return Response('Person is not found')

    serialized_object=PersonSerializer(personal_object,data=request.data)
    if serialized_object.is_valid():
        serialized_object.save()
        return Response(200)

    return Response(serialized_object.errors)

class PersonDelete(APIView):
    def post(self,request,pk):
        try:
            personal_object=Person.object.get(pk=pk)
        except:
            return Response('Person is not found')
        
        personal_object.delete()

        return Response(200)
