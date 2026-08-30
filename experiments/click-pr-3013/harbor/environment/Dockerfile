FROM python:3.13.7-slim-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir uv==0.8.14

WORKDIR /app
RUN git clone https://github.com/pallets/click.git . \
    && git checkout 3be1f33c8e0b13295853f6aa64d1f7412b5312df \
    && git remote remove origin \
    && uv sync --frozen --no-default-groups --group tests

ENV PATH="/app/.venv/bin:${PATH}"
