from django.shortcuts import render
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status


@api_view(['GET'])
def school_list(request):
    if request.method == 'GET':
        school = School.objects.all()
        serializer = SchoolSerializer(school, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def batch_list(request):
    if request.method == 'GET':
        batch = Batch.objects.all()
        serializer = BatchSerializer(batch, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def student_list(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def school_add(request):
    if request.method == 'GET':
        school = School.objects.all()
        serializer = SchoolSerializer(school, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def batch_add(request):
    if request.method == 'GET':
        batch = Batch.objects.all()
        serializer = BatchSerializer(batch, many=True,context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = BatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def student_add(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True,context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def school_delete(request, school_id):
    school = School.objects.get(id=school_id)
    if request.method ==  'GET':
        serializer = SchoolSerializer(school, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PATCH'])
def student_edit(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def school_update(request, school_id):
    try:
        school = School.objects.get(id=school_id)
    except School.DoesNotExist:
        return Response({'error': 'School not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SchoolSerializer(school)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    elif request.method == 'PUT':
        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SchoolWithBatch(APIView):
    def get(self,request,school_id, format=None):
        try:
            school = School.objects.get(id=school_id)
        except School.DoesNotExist:
            return Response({'error': 'School not found '}, status=status.HTTP_404_NOT_FOUND)
        
        school_serializer = SchoolSerializer(school)
        batches = Batch.objects.filter(school=school)
        
        final_data=[]
        for batch in batches:
           
            batch_serializer = BatchSerializer(batch)
            students = Student.objects.filter(batch=batch)
            student_serializer = StudentSerializer(students,many=True)
            
            batch_data = batch_serializer.data
            batch_data['student_data'] = student_serializer.data
            
            final_data.append(batch_data)
            
            
        response_data ={
            'School': school_serializer.data,
            'Batch':final_data
        }    
        return Response(response_data,status=status.HTTP_200_OK)