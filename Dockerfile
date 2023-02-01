# build an image with front and backend for production purposes.

# build first stage with frontend
FROM node:lts as frontend

WORKDIR /opt/app

ARG VERSION
ENV VERSION=$VERSION

COPY services/frontend .

# build frontend with Quasar
# see https://quasar.dev/quasar-cli-vite/commands-list#build
RUN npm i && \
    npm i -g @quasar/cli && \
    cd /opt/app && \
    quasar mode add pwa && \
    quasar build -m pwa

# then build final stage with backend, and frontend copied from first stage
FROM python:3.11-buster

WORKDIR /opt/cenemat

# set environment variables
ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy app
COPY services/backend/src /opt/cenemat
COPY services/backend/requirements.txt /opt/cenemat

# copy SQL migrations
COPY services/sql /opt/sql

# upgrade Debian packages, install Python dependencies, create frontend static directory
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir --upgrade -r /opt/cenemat/requirements.txt && \
    rm /opt/cenemat/requirements.txt && \
    mkdir -p /opt/cenemat/static/frontend

# copy minified files built by Quasar
COPY --from=frontend /opt/app/dist/pwa /opt/cenemat/static/frontend

# expose server port
EXPOSE 8000

# executing command with gunicorn
# see https://www.uvicorn.org/deployment/#gunicorn
CMD ["gunicorn", "main:app", "-w",  "4", "-k", "uvicorn.workers.UvicornWorker"]
