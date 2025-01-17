# Use uma imagem base Python
FROM python:3.12-slim

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:$PATH"

# Configurar o diretório de trabalho
WORKDIR /app

# Instalar dependências necessárias
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -v https://install.python-poetry.org

# Instalar o Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Verificar instalação do Poetry
RUN poetry --version

# Copiar arquivos de dependências
COPY pyproject.toml poetry.lock README.md /app/

# Instalar dependências do projeto com Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --without dev --no-root

# Copiar o código da aplicação
COPY sge_project /app/sge_project

# Expor a porta usada pelo Django
EXPOSE 8000

# Comando padrão para rodar o servidor
CMD ["python", "sge_project/manage.py", "runserver", "0.0.0.0:8000"]
