from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.conf import settings
from django.http import Http404, HttpResponseRedirect
from .models import Course, Registration
from datetime import datetime
import os

from .forms import CustomUserCreationForm

def allCourses(request):
    user = request.user
    if user.is_authenticated:
        courses = Course.objects.all().order_by('start_date')
        registration = Registration.objects.filter(user=user)
        return render(request, os.path.join(settings.BASE_DIR, 'templates', 'courses', 'courses.html'), {'courses': courses, 'registration': registration})
    else:
        return render(request, os.path.join(settings.BASE_DIR, 'templates', 'courses', 'courses.html'))

def registerCourse(request, pk):
    user = request.user
    try:
        course = Course.objects.get(pk=pk)
    except:
        raise Http404
    try:
        registration = Registration.objects.get(user=user, course=course)
        registration.canceled = False
        registration.cancel_date = None
        registration.save()
    except:
        registration = Registration.objects.create(user=user, course=course)
        registration.save()
    return redirect('/')

def unregisterCourse(request, pk):
    user = request.user
    course = Course.objects.get(pk=pk)
    registration = Registration.objects.get(user=user, course=course)
    registration
    registration.canceled = True
    registration.cancel_date = datetime.now()
    registration.save()
    return redirect('/')

def myCourses(request):
    courses = Course.objects.all().order_by('start_date')
    user = request.user
    registration = Registration.objects.filter(user=user)
    return render(request, os.path.join(settings.BASE_DIR, 'templates', 'courses', 'mycourses.html'), {'courses': courses, 'registration': registration})

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'