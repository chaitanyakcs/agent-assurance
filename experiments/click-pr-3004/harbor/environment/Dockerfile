FROM python:3.13.7-slim-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir uv==0.8.14

WORKDIR /app
RUN git clone https://github.com/pallets/click.git . \
    && git checkout a1235aacb1be55dc66ddcfefbf64dec44b6ab54d \
    && git remote remove origin \
    && uv sync --frozen --no-default-groups --group tests

ENV PATH="/app/.venv/bin:${PATH}"
