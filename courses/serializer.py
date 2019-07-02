from rest_framework import serializers
from .models import Course
from students.serializer import SerializerStudent


class SerializerCourses(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'name', 'start_time', 'end_time', 'start_date', 'end_date']


class SerializerCoursesStudents(serializers.ModelSerializer):
    students = SerializerStudent(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
