from rest_framework.viewsets import ModelViewSet
from .models import StudyGroup, Student
from .serializers import StudyGroupSerializer, StudentSerializer

class StudyGroupViewSet(ModelViewSet):
    queryset = StudyGroup.objects.select_related("curator").all()
    serializer_class = StudyGroupSerializer
    filterset_fields = ["course"]

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.select_related("user", "group").all()
    serializer_class = StudentSerializer
    filterset_fields = ["group", "admission_year"]
