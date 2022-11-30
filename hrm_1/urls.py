from django.urls import path
from .views.employee import EmployeeList

urlpatterns = [
    path('employees', EmployeeList.as_view())
]