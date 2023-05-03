FROM nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    curl \
    git \
    graphviz \
    make \
    python3.10-dev \
    sudo \
    wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3.10 -

ENV PATH=/opt/poetry/bin:$PATH

ENV USERNAME=devcontainer
ENV USER_UID=1000
ENV USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -s /usr/bin/bash -m $USERNAME && \
    usermod -aG sudo $USERNAME && \
    echo "${USERNAME} ALL=NOPASSWD:ALL" >> /etc/sudoers

ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=compute,utility
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

USER $USERNAME
