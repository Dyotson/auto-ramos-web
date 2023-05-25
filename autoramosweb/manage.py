#!/usr/bin/env python
***REMOVED***Django's command-line utility for administrative tasks.***REMOVED***
***REMOVED***
import sys


def main(***REMOVED***:
    ***REMOVED***Run administrative tasks.***REMOVED***
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autoramosweb.settings'***REMOVED***
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ***REMOVED*** from exc
    execute_from_command_line(sys.argv***REMOVED***


if __name__ == '__main__':
    main(***REMOVED***
