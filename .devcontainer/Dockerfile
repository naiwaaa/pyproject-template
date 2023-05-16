FROM nvidia/cuda:11.7.1-cudnn8-devel-ubuntu22.04

ARG PYTHON_VERSION

ENV NVIDIA_VISIBLE_DEVICES=all \
    NVIDIA_DRIVER_CAPABILITIES=compute,utility

ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1

ENV PATH="$POETRY_HOME/bin:$PATH" \
    DEBIAN_FRONTEND=noninteractive

RUN export GNUPGHOME="$(mktemp -d)" && \
    gpg --no-default-keyring --lock-never \
        --keyring /usr/share/keyrings/deadsnakes.gpg \
        --keyserver hkp://keyserver.ubuntu.com:80 \
        --recv-keys F23C5A6CF475977595C89F51BA6932366A755776 && \
    echo "deb [signed-by=/usr/share/keyrings/deadsnakes.gpg] https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy main" >> /etc/apt/sources.list && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends \
        curl \
        git \
        graphviz \
        make \
        python$PYTHON_VERSION \
        python$PYTHON_VERSION-dev \
        python-is-python3 \
        sudo \
        wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 -

ENV USERNAME=devcontainer \
    USER_UID=1000 \
    USER_GID=1000

RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -s /usr/bin/bash -m $USERNAME && \
    usermod -aG sudo $USERNAME && \
    echo "${USERNAME} ALL=NOPASSWD:ALL" >> /etc/sudoers

USER $USERNAME
