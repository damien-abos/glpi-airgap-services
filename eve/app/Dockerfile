# syntax=docker/dockerfile:1

ARG BASE_IMAGE_NAME=docker.io/library/python
ARG BASE_IMAGE_TAG=latest

FROM ${BASE_IMAGE_NAME}:${BASE_IMAGE_TAG}

ARG BASE_IMAGE_NAME=docker.io/library/python
ARG BASE_IMAGE_TAG=latest

LABEL org.opencontainers.image.authors="damien-abos"
LABEL org.opencontainers.image.vendor="damien-abos"
LABEL org.opencontainers.image.source="https://github.com/damien-abos/glpi-services"
LABEL org.opencontainers.image.documentation="https://github.com/damien-abos/glpi-services/wiki"
LABEL org.opencontainers.image.url="https://github.com/damien-abos/glpi-services/packages"
LABEL org.opencontainers.image.description="Mock of GLPI services for registration and marketplace"
LABEL org.opencontainers.image.title="docker-glpi-services"
LABEL org.opencontainers.image.licenses="APACHE-2.0"
LABEL org.opencontainers.image.vendor="damien-abos"
LABEL org.opencontainers.image.base.name="${BASE_IMAGE_NAME}:${BASE_IMAGE_TAG}"

LABEL maintainer="damien-abos"


# copy local files
COPY app /app/

# install requiremements
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

#WORKDIR /
EXPOSE 8080
#CMD ["fastapi", "run", "app/main.py", "--proxy-headers", "--port", "8080"]