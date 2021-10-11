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
    poetry export --without-hashes --with-credentials -f requirements.txt > requirements.txt && \
    touch -d @0 requirements.txt && \
    pip freeze | xargs pip uninstall -y

## Install packages
RUN pip install --no-cache --requirement requirements.txt

COPY breach_bot breach_bot

CMD ["python", "-m", "breach_bot.main"]
