#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import json

DIR_PATH_FILE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(DIR_PATH_FILE, '.config_project/conf.json')) as json_file:
    confs = json.loads(json_file.read())


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', confs['generals']['settings'])
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
