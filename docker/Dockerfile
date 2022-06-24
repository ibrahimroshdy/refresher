# Multistage build
# 1. Base image as python for requirments/env
FROM python:3.7-slim-stretch as base
LABEL org.opencontainers.image.source https://github.com/ibrahimroshdy/refresher
RUN apt-get update \
&& apt-get install -y --no-install-recommends git libpq-dev\
&& apt-get purge -y --auto-remove \
&& rm -rf /var/lib/apt/lists/*
COPY .git /app/.git

FROM base as dependencies

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install poetry && \
    poetry config virtualenvs.create false

# copy poetry packages file
COPY pyproject.toml ./
RUN poetry install --no-interaction --no-ansi

# Multistage build
# 2. Changes from the backend files
FROM base as final

# copy installed deps from dependencies image
COPY --from=dependencies /opt/venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 8000
WORKDIR /app

# copying working files at workdir
# Django
COPY manage.py .
COPY config config
COPY apps apps
RUN mkdir static

# Entrypoint script
COPY ./scripts/entrypoint.sh .

# Make file executable
RUN chmod +x entrypoint.sh

# Entrypoint
CMD ["/app/entrypoint.sh"]