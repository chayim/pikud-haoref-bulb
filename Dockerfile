ARG UV_VERSION=${UV_VERSION:-0.10.7}
ARG PYTHON_VERSION=${PYTHON_VERSION:-3.12-slim}

FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv
FROM python:${PYTHON_VERSION} AS builder

ARG PYTHON_VERSION

COPY --from=uv /uv /usr/local/bin/uv
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
WORKDIR /app
COPY pyproject.toml .python-version ./
COPY src/ src/
RUN uv build --wheel && uv pip install --system dist/*.whl

FROM python:${PYTHON_VERSION}
COPY --from=builder /usr/local /usr/local
ENTRYPOINT ["python", "-m", "pikud_haoref_bulb"]
