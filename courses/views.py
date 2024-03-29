from django.shortcuts import render
from rest_framework.views import APIView
from util.ResponseBuilder import Response_Builder
from students.models import Student
from .models import Course
from datetime import datetime
import dateutil.relativedelta
from .serializer import *
from django.db.models import Count
from django.db.models.aggregates import Max
import pytz
import json


Resp = Response_Builder()

# Create your views here.


class AddCourse(APIView):

    def dispatch(self, request, *args, **kwargs):
        return super(AddCourse, self).dispatch(request, *args, **kwargs)

    def post(self, request):

        try:
            name = request.data['name']
            start_time = request.data['start_time']
            end_time = request.data['end_time']
            start_date = request.data['start_date']
            end_date = request.data['end_date']
            number_students = 0

            course = Course()
            course.name = name
            course.start_time = start_time
            course.end_time = end_time
            course.start_date = start_date
            course.end_date = end_date
            course.number_students = number_students
            course.save()

            return Resp.send_response(_status=200, _msg='OK', _data='The course was created successfully.')
        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='The course could not be created.')


class UpdateCourse(APIView):

    def dispatch(self, request, *args, **kwargs):
        return super(UpdateCourse, self).dispatch(request, *args, **kwargs)

    def post(self, request):

        try:
            course_id = request.data['course_id']

            try:
                course = Course.objects.get(id=course_id)
            except:
                return Resp.send_response(_status=503, _msg='The course does not exist.')

            name = request.data['name']
            start_time = request.data['start_time']
            end_time = request.data['end_time']
            start_date = request.data['start_date']
            end_date = request.data['end_date']

            course.name = name
            course.start_time = start_time
            course.end_time = end_time
            course.start_date = start_date
            course.end_date = end_date
            print(course)
            course.save()

            return Resp.send_response(_status=200, _msg='OK', _data='The course was updated successfully.')
        except Exception as e:
            return Resp.send_response(_status=503, _msg='The course could not be updated.')


class ListCourses(APIView):

    def get(self, request, format=None):
        try:
            courses = Course.objects.all()
            serialized_courses = SerializerCourses(courses, many=True)

            return Resp.send_response(_status=200, _msg='OK', _data=serialized_courses.data)

        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='It is not possible to list the courses')


class DeleteCourse(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super(DeleteCourse, self).dispatch(request, *args, **kwargs)

    def post(self, request):

        try:
            course_id = request.data['course_id']

            try:
                course = Course.objects.get(id=course_id)
            except Exception as e:
                return Resp.send_response(_status=503, _msg='The course does not exist.')

            course.delete()

            return Resp.send_response(_status=200, _msg='OK', _data='The course was deleted successfully')

        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='The course could not be deleted.')


class AddStudentCourse(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super(AddStudentCourse, self).dispatch(request, *args, **kwargs)

    def post(self, request):

        try:
            course_id = request.data['course_id']
            students_id = request.data['students_id']

            try:
                course = Course.objects.get(id=course_id)
            except:
                return Resp.send_response(_status=503, _msg='The course does not exist.')

            for student_id in students_id:
                student = Student.objects.get(id=student_id)
                course.students.add(student)

            number_students = course.students.count()
            course.number_students = number_students
            course.save()

            return Resp.send_response(_status=200, _msg='OK', _data='The students were added successfully')

        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='It is not possible to add students.')


class DeleteStudentCourse(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super(DeleteStudentCourse, self).dispatch(request, *args, **kwargs)

    def post(self, request):

        try:
            course_id = request.data['course_id']
            students_id = request.data['students_id']

            try:
                course = Course.objects.get(id=course_id)
            except:
                return Resp.send_response(_status=503, _msg='The course does not exist.')

            for student_id in students_id:
                student = Student.objects.get(id=student_id)
                course.students.remove(student)

            number_students = course.students.count()
            course.number_students = number_students
            course.save()

            return Resp.send_response(_status=200, _msg='OK', _data='The students were deleted successfully')

        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='It is not possible to deleted students.')


class ListCoursesStudents(APIView):

    def get(self, request, format=None):
        try:
            courses = Course.objects.all()
            serialized_courses = SerializerCoursesStudents(courses, many=True)

            return Resp.send_response(_status=200, _msg='OK', _data=serialized_courses.data)

        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='It is not possible to list the courses')


class ListCourseStudents(APIView):

    def get(self, request, format=None):
        try:
            course_id = request.data['course_id']
            courses = Course.objects.filter(id=course_id)
            serialized_courses = SerializerCoursesStudents(courses, many=True)

            return Resp.send_response(_status=200, _msg='OK', _data=serialized_courses.data)

        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='It is not possible to list the courses')


class GetMaxNumberCourses(APIView):
    def dispatch(self, request, *args, **kwargs):
        return super(GetMaxNumberCourses, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        try:
            date_now = datetime.now()

            d2 = date_now - dateutil.relativedelta.relativedelta(months=6)

            print(date_now)
            print(d2)

            courses = Course.objects.filter(start_date__range=[d2, date_now]).annotate(max_value=Max('number_students')).order_by('-max_value')[:3]
            serialized_courses = SerializerCoursesStudents(courses, many=True)

            return Resp.send_response(_status=200, _msg='OK', _data=serialized_courses.data)
        except Exception as e:
            print(e)
            return Resp.send_response(_status=503, _msg='It is not possible to list the courses')

