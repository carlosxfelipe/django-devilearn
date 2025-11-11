from django.urls import path
from . import views

urlpatterns = [
    path("", views.courses_list, name="courses"),
    path("<int:pk>/", views.course_detail, name="course_detail"),
    path("<int:pk>/lessons/", views.course_lessons, name="course_lessons"),
]
