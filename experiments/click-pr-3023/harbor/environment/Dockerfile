FROM python:3.13.7-slim-bookworm
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir uv==0.8.14
WORKDIR /app
RUN git clone https://github.com/pallets/click.git . \
    && git checkout 4f936ac1981645488f396953bc59e50445de00b6 \
    && git remote remove origin \
    && uv sync --frozen --no-default-groups --group tests
ENV PATH="/app/.venv/bin:${PATH}"
