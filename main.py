import os
import django

from django.core.management import execute_from_command_line

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
execute_from_command_line("manage.py runserver localhost:8000".split())

django.setup()
from datacenter.models import *


def main():
    pass


if __name__ == "__main__":
    main()
