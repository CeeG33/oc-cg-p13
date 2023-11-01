import os
import sys


def main():
    """
    Entry point for running the Django project.

    This function is the main entry point for running your Django project.
    It sets the Django settings module, checks for Django's availability, and
    executes commands from the command line.

    Raises:
        ImportError: If Django is not installed or not available on PYTHONPATH.

    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
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
