"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import sys
from pathlib import Path

from django.core.asgi import get_asgi_application

ENTRYPOINT_DIR = Path(__file__).resolve().parent
PROJECT_ROOTS = (
    Path.cwd(),
    Path.cwd() / 'app',
    ENTRYPOINT_DIR,
    ENTRYPOINT_DIR.parent,
    ENTRYPOINT_DIR.parent.parent,
)
for project_root in PROJECT_ROOTS:
    if (project_root / 'app' / 'settings.py').is_file():
        sys.path.insert(0, str(project_root))
        break
else:
    raise RuntimeError(
        'Could not locate app/settings.py. Set the Vercel Root Directory to the '
        'repository root or its app/ directory.'
    )

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_asgi_application()
