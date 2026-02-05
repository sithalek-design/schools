from rest_framework.viewsets import ModelViewSet
from apps.teacher.models import Teacher
from .serializers import TeacherSerializer

class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all().order_by("id")
    serializer_class = TeacherSerializer
