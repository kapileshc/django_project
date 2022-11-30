from django.urls import path
from .views.employee import EmployeeList,EmployeeDetails

urlpatterns = [
    path('employees', EmployeeList.as_view()),
    path('employees/<int:pk>',EmployeeDetails.as_view())
]