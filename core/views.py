from django.shortcuts import render
from rest_framework import status
from .models import Course
from .serializers import Course_serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def course(request,pk=None):
    if request.method == 'GET':
        if pk is not None:
            course = Course.objects.get(id = pk)
            serializer = Course_serializer(course)
            return Response(serializer.data)
        course = Course.objects.all()
        serializer = Course_serializer(course,many = True)  
        return Response(serializer.data) 

    if request.method == 'POST':
        serializer = Course_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data insert successfully!'}
            return Response(res)
        return Response(serializer.errors)    
