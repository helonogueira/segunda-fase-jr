import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vitaclin.settings')

application = get_wsgi_application()

# Cria usuário padrão automaticamente se não existir
try:
    from django.contrib.auth.models import User
    if not User.objects.filter(username='vitaclin').exists():
        User.objects.create_superuser('vitaclin', '', 'vitaclin2026')
except Exception:
    pass