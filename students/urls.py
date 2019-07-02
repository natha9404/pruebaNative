from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('add_student/', AddStudent.as_view()),
    path('update_student/', UpdateStudent.as_view()),
    path('list_students/', ListStudents.as_view()),
    path('delete_student/', DeleteStudents.as_view())

]