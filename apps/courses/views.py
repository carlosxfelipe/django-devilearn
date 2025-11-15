from django.shortcuts import render


def courses_list(request):
    courses = [
        {
            "id": 1,
            "level": "Beginner",
            "rating": 5.0,
            "course_title": "Three-month Course to Learn the Basics of Python and Start Coding.",
            "instructor": "Alison Walsh",
            "course_image": "images/curso_1.jpg",
            "instructor_image": "https://randomuser.me/api/portraits/women/68.jpg",
        },
        {
            "id": 2,
            "level": "Beginner",
            "rating": 5.0,
            "course_title": "Beginner's Guide to Successful Company Management: Business And More",
            "instructor": "Patty Kutch",
            "course_image": "images/curso_2.jpg",
            "instructor_image": "https://randomuser.me/api/portraits/women/20.jpg",
        },
        {
            "id": 3,
            "level": "Beginner",
            "rating": 5.0,
            "course_title": "A Fascinating Theory of Probability. Practice. Application. How to Outplay...",
            "instructor": "Alonzo Murray",
            "course_image": "images/curso_3.jpg",
            "instructor_image": "https://randomuser.me/api/portraits/men/32.jpg",
        },
        {
            "id": 4,
            "level": "Beginner",
            "rating": 5.0,
            "course_title": "Introduction: Machine Learning and LLM. Implementation in Modern Software",
            "instructor": "Gregory Harris",
            "course_image": "images/curso_4.jpg",
            "instructor_image": "https://randomuser.me/api/portraits/men/45.jpg",
        },
    ]
    return render(request, "courses/courses.html", {"courses": courses})


def course_detail(request, pk):
    course = {
        "course_title": "Django Aplicaciones",
        "course_link": "course_lessons",
        "course_image": "images/curso_2.jpg",
        "info_course": {"lessons": 79, "duration": 8, "instructor": "Ricardo Cuéllar"},
        "course_content": [
            {
                "id": 1,
                "name": "Introducción al curso",
                "lessons": [
                    {"name": "¿Qué aprenderás en el curso?", "type": "video"},
                    {"name": "¿Cómo usar la plataforma?", "type": "article"},
                ],
            }
        ],
    }

    return render(request, "courses/course_detail.html", {"pk": pk, "course": course})


def course_lessons(request, pk):
    lesson = {
        "course_title": "Django Aplicaciones",
        "course_progress": 30,
        "course_content": [
            {
                "id": 1,
                "name": "Introducción al curso",
                "total_lessons": 6,
                "complete_lessons": 3,
                "lessons": [
                    {"name": "¿Qué aprenderás en el curso?", "type": "video"},
                    {"name": "¿Cómo usar la plataforma?", "type": "article"},
                ],
            },
            {
                "id": 2,
                "name": "Django principios",
                "total_lessons": 12,
                "complete_lessons": 2,
                "lessons": [
                    {"name": "¿Qué aprenderás en el curso?", "type": "video"},
                    {"name": "¿Cómo usar la plataforma?", "type": "article"},
                ],
            },
        ],
    }

    return render(request, "courses/course_lessons.html", {"pk": pk, "lesson": lesson})
