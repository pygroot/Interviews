from django.urls import path

from . import views 
 
urlpatterns = [ 
    path('api/Persons/', views.Person_list, name="Person_list"),
    
    path('api/Persons/<str:pk>/', views.Person_list_published, name="Person_list_published"),
    path('api/Employees/', views.Employee_list, name="Employee_list"),
  
    path('api/Employees/<str:pk>/', views.Employee_list_published, name="Employee_list_published"),
]


# from django.urls import path

# from . import views 
 
# urlpatterns = [ 
#     path('api/Employees/', views.Person_list, name="Person_list"),
    
#     path('api/Employees/', views.Employee_list, name="Employee_list"),
   
# ]