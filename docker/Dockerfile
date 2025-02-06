# Multistage build to optimize caching 

# 1. Base image as python for system requirment (Installing requirements for debian environment)
FROM python:3.9-slim as base
# Needed by github container registry
LABEL org.opencontainers.image.source https://github.com/ibrahimroshdy/refresher
RUN apt-get update \
&& apt-get install -y --no-install-recommends git libpq-dev gcc python3-dev\
&& apt-get purge -y --auto-remove \
&& rm -rf /var/lib/apt/lists/*

# 2. Python packages and virtual env setup
FROM base as sys_setup

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN python -m venv /opt/venv
# Make sure we use the venv (virtual environment)
ENV PATH="/opt/venv/bin:$PATH"

# Install poetry and configure it
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

# Copy poetry files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Multistage build
# 3. Changes from the backend files
FROM base as final

# copy installed deps from base (known as sys_setup) image
COPY --from=sys_setup /opt/venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 8000
WORKDIR /app

# copying working files at workdir

# Django
COPY manage.py .
COPY refresher_config refresher_config
COPY apps apps
RUN mkdir static

# Entrypoint script
COPY ./scripts/entrypoint.sh .

# Make file executable
RUN chmod +x entrypoint.sh

# Entrypoint
CMD ["/app/entrypoint.sh"]