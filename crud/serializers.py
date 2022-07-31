from rest_framework import serializers
from .models import Student, ClassLevel, School
from users.models import Teacher


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "username", "email", "phone", "class_level", "subject"


class ClassLevelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClassLevel
        fields = "__all__"


class SchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"
