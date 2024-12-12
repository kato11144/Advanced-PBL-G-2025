FROM ubuntu:22.04

WORKDIR /workspace

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo
ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y --no-install-recommends \
    vim \
    tzdata \
    sagemath \
    mysql-server \
    mysql-client \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo "${TZ}" > /etc/timezone

COPY requirements.txt /tmp/requirements.txt
RUN sage -pip install -r /tmp/requirements.txt
