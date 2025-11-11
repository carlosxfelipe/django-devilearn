import subprocess
import sys


def main():
    try:
        subprocess.run(["uv", "run", "python", "manage.py", "runserver"], check=True)
    except KeyboardInterrupt:
        print("\nServidor interrompido pelo usuário.")
    except Exception as e:
        print(f"Erro ao iniciar o servidor: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
