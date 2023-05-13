FROM nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu22.04

ENV \
    NVIDIA_VISIBLE_DEVICES=all \
    NVIDIA_DRIVER_CAPABILITIES=compute,utility

ENV \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

ENV \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    VENV_PATH="$PROJECT_PATH/.venv"

ENV PATH="$VENV_PATH/bin:$POETRY_HOME/bin:$PATH"
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
    rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3.10 -

ENV USERNAME=devcontainer
ENV USER_UID=1000
ENV USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -s /usr/bin/bash -m $USERNAME && \
    usermod -aG sudo $USERNAME && \
    echo "${USERNAME} ALL=NOPASSWD:ALL" >> /etc/sudoers

USER $USERNAME
