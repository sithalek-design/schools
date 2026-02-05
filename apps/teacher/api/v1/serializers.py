from rest_framework import serializers
from apps.teacher.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
