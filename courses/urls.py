from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('add_course/', AddCourse.as_view()),
    path('update_course/', UpdateCourse.as_view()),
    path('list_courses/', ListCourses.as_view()),
    path('delete_course/', DeleteCourse.as_view()),
    path('add_student_course/', AddStudentCourse.as_view()),
    path('delete_student_course/', DeleteStudentCourse.as_view()),
    path('list_students_courses/', ListCoursesStudents.as_view()),
    path('list_students_course/', ListCourseStudents.as_view()),
    path('get_max_number_courses/', GetMaxNumberCourses.as_view())
]