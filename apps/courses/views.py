from django.shortcuts import render


def courses_list(request):
    courses = [
        {
            "id": 1,
            "level": "Principiante",
            "rating": 5.0,
            "course_title": "Curso de tres meses para aprender lo básico de Python y empezar a programar.",
            "instructor": "Alison Walsh",
            "course_image": "images/curso_1.jpg",
            "instructor_image": "https://randomuser.me/api/portraits/women/68.jpg",
        },
        {
            "id": 2,
            "level": "Principiante",
            "rating": 5.0,
            "course_title": "Guía para principiantes sobre gestión empresarial exitosa: negocios y más",
            "instructor": "Patty Kutch",
            "course_image": "images/curso_2.jpg",
            "instructor_image": "https://randomuser.me/api/portraits/women/20.jpg",
        },
        {
            "id": 3,
            "level": "Principiante",
            "rating": 5.0,
            "course_title": "Una fascinante teoría de la probabilidad. Práctica. Aplicación. Cómo ganar...",
            "instructor": "Alonzo Murray",
            "course_image": "images/curso_3.jpg",
            "instructor_image": "https://randomuser.me/api/portraits/men/32.jpg",
        },
        {
            "id": 4,
            "level": "Principiante",
            "rating": 5.0,
            "course_title": "Introducción: Machine Learning y LLM. Implementación en software moderno",
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
