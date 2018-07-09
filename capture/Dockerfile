FROM alpine

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
    && apk add --no-cache py-virtualenv python3 \
    # MySQL / MariaDB
    && apk add --no-cache mariadb mariadb-dev mariadb-client

RUN apk add --no-cache gcc

ADD ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

USER root

WORKDIR $APP
