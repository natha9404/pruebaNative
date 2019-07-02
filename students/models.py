from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    email = models.EmailField()

    def __str__(self):
        return '%s %s' % (self.name, self.last_name)