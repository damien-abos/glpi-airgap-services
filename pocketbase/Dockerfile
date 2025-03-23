# syntax=docker/dockerfile:1

ARG BASE_IMAGE_NAME=docker.io/library/alpine
ARG BASE_IMAGE_TAG=latest

FROM ${BASE_IMAGE_NAME}:${BASE_IMAGE_TAG}

ARG BASE_IMAGE_NAME=docker.io/library/alpine
ARG BASE_IMAGE_TAG=latest
ARG PB_VERSION=0.26.1

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

RUN apk add --no-cache \
    unzip \
    ca-certificates

# download and unzip PocketBase
ADD https://github.com/pocketbase/pocketbase/releases/download/v${PB_VERSION}/pocketbase_${PB_VERSION}_linux_amd64.zip /tmp/pb.zip
RUN unzip /tmp/pb.zip -d /app/

# uncomment to copy the local pb_migrations dir into the image
# COPY ./pb_migrations /app/pb_migrations

# uncomment to copy the local pb_hooks dir into the image
# COPY ./pb_hooks /app/pb_hooks

COPY app /app/

EXPOSE 8080

# start PocketBase
CMD ["/app/pocketbase", "serve", "--http=0.0.0.0:8080"]