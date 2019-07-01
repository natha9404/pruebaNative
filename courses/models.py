from django.db import models
from students.models import Student


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField()
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name