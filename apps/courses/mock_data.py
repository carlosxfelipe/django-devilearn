courses = [
    {
        "id": 1,
        "level": "Principiante",
        "rating": 5.0,
        "course_title": "Python: Fundamentos hasta los Detalles",
        "description": "Curso intensivo de introducción a Python. Cubre desde sintaxis básica y estructuras de datos hasta buenas prácticas y detalles avanzados para escribir código confiable.",
        "duration": "3 meses",
        "language": "Español",
        "tags": ["python", "fundamentos", "programación"],
        "instructor": "Alison Walsh",
        "course_image": "images/curso_1.jpg",
        "instructor_image": "https://randomuser.me/api/portraits/women/68.jpg",
    },
    {
        "id": 2,
        "level": "Principiante",
        "rating": 5.0,
        "course_title": "Django: Crea Aplicaciones Robustas",
        "description": "Guía práctica para construir aplicaciones web sólidas con Django: modelos, vistas, plantillas, autenticación y despliegue básico.",
        "duration": "2 meses",
        "language": "Español",
        "tags": ["django", "web", "backend"],
        "instructor": "Patty Kutch",
        "course_image": "images/curso_2.jpg",
        "instructor_image": "https://randomuser.me/api/portraits/women/20.jpg",
    },
    {
        "id": 3,
        "level": "Avanzado",
        "rating": 5.0,
        "course_title": "Django Avanzado",
        "description": "Profundiza en Django: optimización, arquitectura, seguridad, pruebas, despliegue en producción y patrones para proyectos escalables.",
        "duration": "2 meses",
        "language": "Español",
        "tags": ["django", "avanzado", "devops"],
        "instructor": "Alonzo Murray",
        "course_image": "images/curso_3.jpg",
        "instructor_image": "https://randomuser.me/api/portraits/men/32.jpg",
    },
    {
        "id": 4,
        "level": "Avanzado",
        "rating": 5.0,
        "course_title": "FastAPI Avanzado",
        "description": "Aprende a desarrollar APIs de alto rendimiento con FastAPI: diseño de endpoints, validación, autenticación, testing y despliegue moderno.",
        "duration": "1.5 meses",
        "language": "Español",
        "tags": ["fastapi", "api", "python"],
        "instructor": "Gregory Harris",
        "course_image": "images/curso_4.jpg",
        "instructor_image": "https://randomuser.me/api/portraits/men/45.jpg",
    },
]

course_details = [
    {
        "course_title": "Python: Fundamentos hasta los Detalles",
        "course_link": "course_lessons",
        "course_image": "images/curso_1.jpg",
        "info_course": {
            "lessons": 60,
            "duration": 12,
            "instructor": "Alison Walsh",
        },
        "course_content": [
            {
                "id": 1,
                "name": "Introducción a Python",
                "lessons": [
                    {
                        "name": "¿Qué aprenderás en este curso de Python?",
                        "type": "video",
                    },
                    {
                        "name": "Instalación del entorno y primeros pasos",
                        "type": "article",
                    },
                ],
            },
            {
                "id": 2,
                "name": "Fundamentos del lenguaje",
                "lessons": [
                    {
                        "name": "Variables, tipos de datos y operadores",
                        "type": "video",
                    },
                    {"name": "Estructuras condicionales", "type": "video"},
                    {"name": "Bucles y control de flujo", "type": "article"},
                ],
            },
            {
                "id": 3,
                "name": "Colecciones y manejo de datos",
                "lessons": [
                    {"name": "Listas y tuplas", "type": "video"},
                    {"name": "Diccionarios y conjuntos", "type": "video"},
                    {"name": "Comprensión de listas", "type": "article"},
                ],
            },
            {
                "id": 4,
                "name": "Funciones y módulos",
                "lessons": [
                    {"name": "Creación y uso de funciones", "type": "video"},
                    {"name": "Argumentos, retorno y ámbito", "type": "article"},
                    {"name": "Módulos y paquetes nativos", "type": "video"},
                ],
            },
            {
                "id": 5,
                "name": "Python práctico",
                "lessons": [
                    {"name": "Trabajo con archivos", "type": "video"},
                    {"name": "Errores y excepciones", "type": "article"},
                    {"name": "Mini-proyecto final", "type": "video"},
                ],
            },
        ],
    },
    {
        "course_title": "Django: Crea Aplicaciones Robustas",
        "course_link": "course_lessons",
        "course_image": "images/curso_2.jpg",
        "info_course": {
            "lessons": 70,
            "duration": 10,
            "instructor": "Patty Kutch",
        },
        "course_content": [
            {
                "id": 1,
                "name": "Introducción a Django",
                "lessons": [
                    {"name": "¿Qué es Django y para qué se usa?", "type": "video"},
                    {"name": "Arquitectura MVT", "type": "article"},
                ],
            },
            {
                "id": 2,
                "name": "Modelos y base de datos",
                "lessons": [
                    {"name": "Creación de modelos en Django", "type": "video"},
                    {"name": "Migraciones y ORM", "type": "article"},
                ],
            },
            {
                "id": 3,
                "name": "Vistas y rutas",
                "lessons": [
                    {"name": "Vistas basadas en funciones", "type": "video"},
                    {"name": "Vistas basadas en clases", "type": "video"},
                    {"name": "URLs y organización del proyecto", "type": "article"},
                ],
            },
            {
                "id": 4,
                "name": "Templates y front-end",
                "lessons": [
                    {"name": "Sistema de plantillas de Django", "type": "video"},
                    {
                        "name": "Uso de bloques, herencia y contexto",
                        "type": "article",
                    },
                ],
            },
            {
                "id": 5,
                "name": "Autenticación y seguridad",
                "lessons": [
                    {"name": "Sistema de usuarios", "type": "video"},
                    {"name": "Protección de rutas y roles", "type": "article"},
                ],
            },
        ],
    },
    {
        "course_title": "Django Avanzado",
        "course_link": "course_lessons",
        "course_image": "images/curso_3.jpg",
        "info_course": {
            "lessons": 50,
            "duration": 8,
            "instructor": "Alonzo Murray",
        },
        "course_content": [
            {
                "id": 1,
                "name": "Optimización avanzada",
                "lessons": [
                    {"name": "Consultas complejas con ORM", "type": "video"},
                    {"name": "Indexación y performance", "type": "article"},
                ],
            },
            {
                "id": 2,
                "name": "Arquitectura y escalabilidad",
                "lessons": [
                    {
                        "name": "Patrón de servicios y apps desacopladas",
                        "type": "video",
                    },
                    {"name": "Uso de Redis y caching", "type": "video"},
                ],
            },
            {
                "id": 3,
                "name": "Seguridad en Django",
                "lessons": [
                    {
                        "name": "Protección CSRF, XSS y SQL Injection",
                        "type": "video",
                    },
                    {"name": "Gestión de permisos y sesiones", "type": "article"},
                ],
            },
            {
                "id": 4,
                "name": "Testing y calidad",
                "lessons": [
                    {"name": "Pruebas unitarias y de integración", "type": "video"},
                    {"name": "Buenas prácticas de cobertura", "type": "article"},
                ],
            },
            {
                "id": 5,
                "name": "Despliegue",
                "lessons": [
                    {"name": "Despliegue con Docker", "type": "video"},
                    {"name": "Configuración en producción", "type": "article"},
                ],
            },
        ],
    },
    {
        "course_title": "FastAPI Avanzado",
        "course_link": "course_lessons",
        "course_image": "images/curso_4.jpg",
        "info_course": {
            "lessons": 80,
            "duration": 12,
            "instructor": "Gregory Harris",
        },
        "course_content": [
            {
                "id": 1,
                "name": "Introducción a FastAPI",
                "lessons": [
                    {"name": "Core de FastAPI y ASGI", "type": "video"},
                    {
                        "name": "Estructura profesional de proyecto",
                        "type": "article",
                    },
                ],
            },
            {
                "id": 2,
                "name": "APIs avanzadas",
                "lessons": [
                    {"name": "Validación avanzada con Pydantic", "type": "video"},
                    {"name": "Rutas, dependencias y seguridad", "type": "article"},
                ],
            },
            {
                "id": 3,
                "name": "Alto rendimiento",
                "lessons": [
                    {"name": "Concurrency con async/await", "type": "video"},
                    {"name": "Optimización y caché", "type": "article"},
                ],
            },
            {
                "id": 4,
                "name": "Integraciones",
                "lessons": [
                    {"name": "FastAPI + SQLAlchemy", "type": "video"},
                    {"name": "Autenticación JWT y OAuth2", "type": "video"},
                ],
            },
            {
                "id": 5,
                "name": "Testing y despliegue",
                "lessons": [
                    {"name": "Testing automático de endpoints", "type": "video"},
                    {
                        "name": "Despliegue con Docker y servidores ASGI",
                        "type": "article",
                    },
                ],
            },
        ],
    },
]

lessons_details = [
    {
        "course_title": "Python: Fundamentos hasta los Detalles",
        "course_progress": 30,
        "course_content": [
            {
                "id": 1,
                "name": "Introducción a Python",
                "total_lessons": 6,
                "complete_lessons": 3,
                "lessons": [
                    {"name": "¿Qué aprenderás en este curso?", "type": "video"},
                    {
                        "name": "Instalación del entorno y primeros pasos",
                        "type": "article",
                    },
                ],
            },
            {
                "id": 2,
                "name": "Fundamentos del lenguaje",
                "total_lessons": 10,
                "complete_lessons": 5,
                "lessons": [
                    {
                        "name": "Variables, tipos de datos y operadores",
                        "type": "video",
                    },
                    {"name": "Condicionales y bucles", "type": "article"},
                ],
            },
        ],
    },
    {
        "course_title": "Django: Crea Aplicaciones Robustas",
        "course_progress": 60,
        "course_content": [
            {
                "id": 1,
                "name": "Introducción a Django",
                "total_lessons": 8,
                "complete_lessons": 6,
                "lessons": [
                    {"name": "¿Qué es Django y para qué se usa?", "type": "video"},
                    {
                        "name": "Arquitectura MVT y creación del proyecto",
                        "type": "article",
                    },
                ],
            },
            {
                "id": 2,
                "name": "Modelos y base de datos",
                "total_lessons": 7,
                "complete_lessons": 2,
                "lessons": [
                    {"name": "Modelos, ORM y migraciones", "type": "video"},
                    {"name": "Relaciones entre tablas", "type": "article"},
                ],
            },
        ],
    },
    {
        "course_title": "Django Avanzado",
        "course_progress": 45,
        "course_content": [
            {
                "id": 1,
                "name": "Optimización avanzada",
                "total_lessons": 5,
                "complete_lessons": 2,
                "lessons": [
                    {
                        "name": "Consultas complejas y optimización con ORM",
                        "type": "video",
                    },
                    {"name": "Buenas prácticas de arquitectura", "type": "article"},
                ],
            },
            {
                "id": 2,
                "name": "Escalabilidad y seguridad",
                "total_lessons": 6,
                "complete_lessons": 1,
                "lessons": [
                    {"name": "Caché, Redis y rendimiento", "type": "video"},
                    {
                        "name": "Protección XSS, CSRF y permisos avanzados",
                        "type": "article",
                    },
                ],
            },
        ],
    },
    {
        "course_title": "FastAPI Avanzado",
        "course_progress": 10,
        "course_content": [
            {
                "id": 1,
                "name": "Introducción a FastAPI",
                "total_lessons": 12,
                "complete_lessons": 2,
                "lessons": [
                    {
                        "name": "FastAPI, ASGI y conceptos iniciales",
                        "type": "video",
                    },
                    {
                        "name": "Estructura profesional del proyecto",
                        "type": "article",
                    },
                ],
            },
            {
                "id": 2,
                "name": "APIs avanzadas",
                "total_lessons": 8,
                "complete_lessons": 0,
                "lessons": [
                    {
                        "name": "Pydantic avanzado y validación profunda",
                        "type": "video",
                    },
                    {
                        "name": "Autenticación moderna (JWT / OAuth2)",
                        "type": "article",
                    },
                ],
            },
        ],
    },
]
