FROM python:3.13.7-slim-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir uv==0.8.14

WORKDIR /app
RUN git clone https://github.com/pallets/click.git . \
    && git checkout 011b9f9d190c71310264e6c54bae6259f5e38a9f \
    && git remote remove origin \
    && uv sync --frozen --no-default-groups --group tests

ENV PATH="/app/.venv/bin:${PATH}"
