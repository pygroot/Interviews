
from rest_framework import serializers
from . import models

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = '__all__'
        
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'      