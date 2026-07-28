import os
import sys
from pathlib import Path

# Fix path navigation: Move up past the inner folders to find 'store'
CURRENT_DIR = Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent.parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(CURRENT_DIR))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppointEase.settings')

application = get_wsgi_application()
