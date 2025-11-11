from django.shortcuts import render


def courses_list(request):
    courses = [
        {
            "id": 1,
            "level": "Beginner",
            "rating": 5.0,
            "course_title": "Three-month Course to Learn the Basics of Python and Start Coding.",
            "instructor": "Alison Walsh",
        },
        {
            "id": 2,
            "level": "Beginner",
            "rating": 5.0,
            "course_title": "Beginner's Guide to Successful Company Management: Business And More",
            "instructor": "Patty Kutch",
        },
        {
            "id": 3,
            "level": "Beginner",
            "rating": 5.0,
            "course_title": "A Fascinating Theory of Probability. Practice. Application. How to Outplay...",
            "instructor": "Alonzo Murray",
        },
        {
            "id": 4,
            "level": "Beginner",
            "rating": 5.0,
            "course_title": "Introduction: Machine Learning and LLM. Implementation in Modern Software",
            "instructor": "Gregory Harris",
        },
    ]
    return render(request, "courses/courses.html", {"courses": courses})


def course_detail(request, pk):
    return render(request, "courses/course_detail.html", {"pk": pk})


def course_lessons(request, pk):
    return render(request, "courses/course_lessons.html", {"pk": pk})
