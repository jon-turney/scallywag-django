"""
WSGI config for scallywag project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import sys
import os

from django.core.wsgi import get_wsgi_application

# ensure the project is in the pythonpath
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scallywag.settings")

application = get_wsgi_application()
