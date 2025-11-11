from django.shortcuts import render


def courses_list(request):
    return render(request, "courses/courses.html")


def course_detail(request, pk):
    return render(request, "courses/course_detail.html", {"pk": pk})


def course_lessons(request, pk):
    return render(request, "courses/course_lessons.html", {"pk": pk})
