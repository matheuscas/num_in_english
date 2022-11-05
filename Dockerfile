FROM python:3.10-alpine

# disables an automatic check for pip updates each time
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
# means Python will not try to write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# ensures our console output is not buffered by Docker
ENV PYTHONUNBUFFERED 1

RUN apk update && apk upgrade
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev
WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml /usr/src/app/
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install -n --no-ansi

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]