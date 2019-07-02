from django.shortcuts import render
from rest_framework.views import APIView
from util.ResponseBuilder import Response_Builder
from .models import Student
from datetime import datetime
from .serializer import *
import pytz
import json


Resp = Response_Builder()

# Create your views here.


class AddStudent(APIView):

    def dispatch(self, request, *args, **kwargs):
        return super(AddStudent, self).dispatch(request, *args, **kwargs)

    def post(self, request):

        try:
            name = request.data['name']
            last_name = request.data['last_name']
            age = request.data['age']
            email = request.data['email']

            student = Student()
            student.name = name
            student.last_name = last_name
            student.age = age
            student.email = email
            student.save()

            return Resp.send_response(_status=200, _msg='OK', _data='The student was created successfully.')
        except Exception as e:
            return Resp.send_response(_status=503, _msg='The student could not be created.')


class UpdateStudent(APIView):

    def dispatch(self, request, *args, **kwargs):
        return super(UpdateStudent, self).dispatch(request, *args, **kwargs)

    def post(self, request):

        try:
            student_id = request.data['student_id']

            try:
                student = Student.objects.get(id=student_id)
            except:
                return Resp.send_response(_status=503, _msg='The student does not exist.')

            name = request.data['name']
            last_name = request.data['last_name']
            age = request.data['age']
            email = request.data['email']

            student.name = name
            student.last_name = last_name
            student.age = age
            student.email = email
            student.save()

            return Resp.send_response(_status=200, _msg='OK', _data='The student was updated successfully.')
        except Exception as e:
            return Resp.send_response(_status=503, _msg='The student could not be updated.')


class ListStudents(APIView):

    def get(self, request, format=None):
        try:
            students = Student.objects.all()
            serialized_students = SerializerStudent(students, many=True)

            return Resp.send_response(_status=200, _msg='OK', _data=serialized_students.data)

        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='It is not possible to list the students')


class DeleteStudents(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super(DeleteStudents, self).dispatch(request, *args, **kwargs)

    def post(self, request):

        try:
            student_id = request.data['student_id']

            try:
                student = Student.objects.get(id=student_id)
            except:
                return Resp.send_response(_status=503, _msg='The student does not exist.')

            student.delete()

            return Resp.send_response(_status=200, _msg='OK', _data='The student was deleted successfully')

        except Exception as e:
            return Resp.send_response(_status=503, _msg='The student could not be deleted.')

