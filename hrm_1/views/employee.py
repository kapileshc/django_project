from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from hrm_1.models import Employee
from hrm_1.serializers import EmployeeSerializer

class EmployeeList(APIView):

    def get(self,request,format=None):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

