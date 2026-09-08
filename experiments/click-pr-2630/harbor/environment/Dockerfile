FROM python:3.13.7-slim-bookworm
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir uv==0.8.14
WORKDIR /app
RUN git clone https://github.com/pallets/click.git . \
    && git checkout 0d69b6ce8b25fe31ea580c608adb8e45df3805bb \
    && git remote remove origin \
    && uv venv \
    && uv pip install -e . \
    && uv pip install -r requirements/typing.txt
ENV PATH="/app/.venv/bin:${PATH}"
