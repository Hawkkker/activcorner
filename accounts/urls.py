from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', views.allCourses, name='courses'),
    path('register/<int:pk>/', views.registerCourse, name='register'),
    path('unregister/<int:pk>/', views.unregisterCourse, name='unregister'),
    path('mycourses/', views.myCourses, name='mycourses'),
]