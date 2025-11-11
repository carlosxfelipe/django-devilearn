## Devilearn — Projeto em Django

Este projeto é uma aplicação Django para gerenciar e exibir cursos em formato de vídeo.

### Pré-requisitos

- [Python](https://www.python.org/) instalado
- [uv](https://github.com/charliermarsh/uv) instalado para executar comandos

### Como iniciar o projeto

1. **Aplicar as migrações do banco de dados:**

   ```bash
   uv run python manage.py migrate
   ```

2. **Executar o servidor de desenvolvimento:**

   Você pode escolher uma das opções abaixo:

   ```bash
   uv run python manage.py runserver
   ```

   ou simplesmente:

   ```bash
   uv run dev.py
   ```

---

### Histórico

O app `courses` foi criado com o comando:

```bash
uv run python manage.py startapp courses
```

O app `dashboard` foi criado com o comando:

```bash
uv run python manage.py startapp dashboard
```

O app `profiles` foi criado com o comando:

```bash
uv run python manage.py startapp profiles
```

Consulte a documentação do Django para mais comandos e opções.
