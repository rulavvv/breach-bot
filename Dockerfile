FROM python:3.9-slim as base
ARG TOKEN

WORKDIR /project

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends libffi-dev ffmpeg

COPY voices voices

COPY ./poetry.lock ./
COPY ./pyproject.toml ./

RUN pip install poetry && \
    poetry install

COPY breach_bot breach_bot

CMD ["poetry", "run", "python", "-m", "breach_bot.main"]
