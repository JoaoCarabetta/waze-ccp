FROM python:3.6.5-alpine3.7

ENV USER_NAME=kratos
ENV USER_HOME=/home/$USER_NAME
ENV APP=/app

RUN set -x && \
    # Install main packages
    apk add --no-cache git tar zip unzip bash make curl wget

# Create user
RUN adduser -D -u 501 -s /bin/bash $USER_NAME

# Create projeto dir
RUN set -x \
    && mkdir -p $APP \
    && chown -R $USER_NAME.$USER_NAME $APP

# Bash setup
RUN set -x \
    # Colorful root bash
    && echo 'export PS1="\e[1m\e[91mGodOfWar\e[39m:\e[96m\w\e[0m# "' > /root/.bashrc \
    # Colorful limited user bash
    && echo 'export PS1="\e[1m\e[32m\\u\e[39m@\e[34masgard\e[39m:\e[96m\w\e[0m$ "' > $USER_HOME/.bashrc

# Python dependencies
RUN set -x \
    && apk add --no-cache py-virtualenv \
    # MySQL / MariaDB
    && apk add --update --no-cache mariadb-client-libs \
	&& apk add --no-cache --virtual .build-deps mariadb-dev gcc musl-dev


ADD ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

USER root

WORKDIR $APP
