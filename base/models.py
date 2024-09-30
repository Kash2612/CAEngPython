from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrolled_date = models.DateField()

    def __str__(self):
        return self.name
