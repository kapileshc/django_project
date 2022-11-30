from rest_framework import serializers

from hrm_1.models import Employee,Attendance

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"

class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = "__all__"



