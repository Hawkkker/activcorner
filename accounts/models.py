from django.contrib.auth.models import AbstractUser
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField('description', blank=True)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    courses = models.ManyToManyField(Course, blank=True, through='Registration', related_name='User_to_course')

    def __str__(self):
        return self.username

class Registration(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    canceled = models.BooleanField(default=False)
    cancel_date = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    