FROM python:3.9-slim

LABEL org.opencontainers.image.source https://github.com/ibrahimroshdy/refresher

# Set Python environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        libpq-dev \
        gcc \
        python3-dev \
        libyaml-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install poetry and dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir poetry coverage && \
    poetry config virtualenvs.create false

# Copy dependency files and install
COPY pyproject.toml ./
RUN poetry install --no-interaction --no-ansi --no-root

# Copy application files
COPY manage.py .
COPY refresher_config refresher_config/
COPY apps apps/
COPY ./scripts/entrypoint.sh .

# Create static directory and set permissions
RUN mkdir static && \
    chmod +x entrypoint.sh

EXPOSE 8000

CMD ["/app/entrypoint.sh"]