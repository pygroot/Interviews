from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Person, Employee
from .serializers import PersonSerializer, EmployeeSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def Person_list(request):
    if request.method == 'GET':
        Persons = Person.objects.all()
        
        name = request.query_params.get('name', None)
        if name is not None:
            Persons = Persons.filter(name__icontains=name)
        
        Persons_serializer = PersonSerializer(Persons, many=True)
        return JsonResponse(Persons_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        Person_data = JSONParser().parse(request)
        Person_serializer = PersonSerializer(data=Person_data)
        if Person_serializer.is_valid():
            Person_serializer.save()
            return JsonResponse(Person_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(Person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Person.objects.all().delete()
        return JsonResponse({'message': '{} Persons were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST', 'DELETE'])
def Employee_list(request):
    if request.method == 'GET':
        Employees = Employee.objects.all()
        
        department = request.query_params.get('department', None)
        if department is not None:
            Employees = Employees.filter(department__icontains=department)
        
        Employees_serializer = EmployeeSerializer(Employees, many=True)
        return JsonResponse(Employees_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        Employee_data = JSONParser().parse(request)
        Employee_serializer = EmployeeSerializer(data=Employee_data)
        if Employee_serializer.is_valid():
            Employee_serializer.save()
            return JsonResponse(Employee_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(Employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Employee.objects.all().delete()
        return JsonResponse({'message': '{} Employees were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
    
    
    
    
@api_view(['GET', 'POST', 'DELETE'])
def Employee_list_published(request,pk):
    tutorials = Employee.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = EmployeeSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False) 
    
    
@api_view(['GET', 'POST', 'DELETE'])
def Person_list_published(request,pk):
    tutorials = Person.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = PersonSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)       