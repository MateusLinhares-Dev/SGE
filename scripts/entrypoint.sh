#!bin/bash

# Rodar migrações do Django
python /app/sge_project/manage.py migrate

# Criar o superusuário, se não existir (opcional)

echo "Creating superuser..."
python /app/sge_project/manage.py shell -c "
import os
from django.contrib.auth.models import User;
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(username='admin', email='admin@example.com', password='admin')
"

# Executar o runserver do django
poetry run manage-django