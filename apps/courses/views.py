from django.shortcuts import render
from .mock_data import courses, course_details, lessons_details


def courses_list(request):
    return render(request, "courses/courses.html", {"courses": courses})


def course_detail(request, pk):
    # Seleciona o curso pelo pk (id)
    pk_int = int(pk)
    if 1 <= pk_int <= len(course_details):
        course = course_details[pk_int - 1]
    else:
        course = course_details[0]

    return render(request, "courses/course_detail.html", {"pk": pk, "course": course})


def course_lessons(request, pk):
    pk_int = int(pk)
    if 1 <= pk_int <= len(lessons_details):
        lesson = lessons_details[pk_int - 1]
    else:
        lesson = lessons_details[0]

    return render(request, "courses/course_lessons.html", {"pk": pk, "lesson": lesson})
