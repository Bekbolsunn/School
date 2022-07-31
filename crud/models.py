from django.db import models
from users.models import Teacher


class Student(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    date_of_birth = models.DateField()
    class_level = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    USER_GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
        ("Animal", "Animal"),
    )
    gender = models.CharField(max_length=10, choices=USER_GENDER, null=True, blank=True)

    def __str__(self):
        return self.name


class ClassLevel(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name="Ученики", blank=True)

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=300)
    classes = models.CharField(max_length=200)

    def __str__(self):
        return self.name
