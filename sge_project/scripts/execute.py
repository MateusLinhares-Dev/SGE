import os


def run_manage():
    os.system("python manage.py runserver 0.0.0.0:8000")


if __name__ == "__main__":
    run_manage()
