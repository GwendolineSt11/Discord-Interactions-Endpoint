"""
WSGI config for discord_interaction project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discord_interaction.settings')
application = get_wsgi_application()

if __name__ == 'discord_interaction':
    from django.core.management import execute_from_command_line
    execute_from_command_line(["manage.py", "runserver", "3000"])
    application.run()
