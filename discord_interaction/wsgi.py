"""
WSGI config for discord_interaction project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from discord_interaction.app import create_app_instance

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'discord_interaction.settings')

application = get_wsgi_application()
