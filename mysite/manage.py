#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from mysite.settings import BASE_DIR

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # try:
    #     if sys.argv[2] == 'react':
    #         project_root = os.getcwd()

    #         os.chdir(os.path.join("C:\\Users\\ayaan\\Desktop\\amtolit\\", "frontend"))
    #         os.system('npm run build')
    #         os.system('npm start')
    #         os.chdir(project_root)
    #         sys.argv.pop(2)
    # except IndexError:
    #     execute_from_command_line(sys.argv)
    # else:
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
