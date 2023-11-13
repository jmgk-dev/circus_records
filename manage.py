#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    server_env = os.environ.get('SERVER_ENV', 'dev')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"circus_site_2023.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
