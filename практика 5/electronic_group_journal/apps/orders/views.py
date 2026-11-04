from rest_framework.viewsets import ModelViewSet
from .models import Lesson, Grade, Attendance
from .serializers import LessonSerializer, GradeSerializer, AttendanceSerializer

class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.select_related("group", "subject", "teacher").all()
    serializer_class = LessonSerializer
    filterset_fields = ["group", "subject", "teacher", "lesson_date"]

class GradeViewSet(ModelViewSet):
    queryset = Grade.objects.select_related("student", "lesson").all()
    serializer_class = GradeSerializer
    filterset_fields = ["student", "lesson", "value"]

class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.select_related("student", "lesson").all()
    serializer_class = AttendanceSerializer
    filterset_fields = ["student", "lesson", "status"]
