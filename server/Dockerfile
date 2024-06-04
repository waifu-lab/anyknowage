FROM python:3.11-buster as build

RUN pip install poetry==1.8.3

ENV POETRY_CACHE_DIR=/tmp/poetry_cache \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    VIRTUAL_ENV=/app/.venv

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create true \
    && poetry install && rm -rf $POETRY_CACHE_DIR

FROM python:3.11-slim-buster as runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

RUN apt-get update && apt-get install -y \
    pandoc

COPY --from=build ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY . .

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]