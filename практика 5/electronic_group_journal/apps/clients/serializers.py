from rest_framework import serializers
from .models import StudyGroup, Student

class StudyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="user.full_name", read_only=True)
    class Meta:
        model = Student
        fields = "__all__"
