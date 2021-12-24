from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    create_datetime = models.DateTimeField()
    modify_datetime = models.DateTimeField()
    
    

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    person_id = models.ForeignKey(Person, on_delete=CASCADE)
    department = models.CharField(max_length=200)
    role = models.CharField(max_length=20)
    line_manager = models.CharField(max_length=200)
    create_datetime = models.DateTimeField()
    modifiy_datetime = models.DateTimeField()
    

    def __str__(self):
        return self.department


