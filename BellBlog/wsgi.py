"""
WSGI config for BellBlog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from mezzanine.utils.conf import real_project_name

<<<<<<< HEAD

=======
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings.local")
>>>>>>> parent of 4fb5ddd (fix: deploy settings)
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "%s.settings" % real_project_name("BellBlog"))

application = get_wsgi_application()
