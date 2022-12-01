FROM python:3.9-slim
LABEL maintainer = "Aaron Garibay <aaron.contreras@unosquare.com>"

# Configure Poetry
ENV POETRY_VERSION=1.2.2 \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    ENVIRONMENT=production

RUN pip install "poetry==$POETRY_VERSION" \
    && pip install "uvicorn[standard]==0.20.0" \
    && pip install "gunicorn==20.1.0"

WORKDIR /
COPY poetry.lock pyproject.toml /

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY html_utils /html_utils

CMD ["poetry", "run", "uvicorn", "main:app", "--app-dir", "html_utils/", "--port", "80", "--host", "0.0.0.0"]
