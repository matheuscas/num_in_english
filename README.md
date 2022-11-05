# English numbers to its full written version

## Description

This project exposes two endpoints:

```shell
GET /num_to_english?number=12345678
```

```shell
POST /num_to_english { "number": "12345678" }
```

This endpoints will convert any number given to it into the english words that describe that number. 
For example the above request should return:

```json
{
  "status": "ok",
  "num_in_english": "twelve million three hundred forty five thousand six hundred seventy eight" 
}
```

Status is reserved for messaging back if the process succeeded or failed.

## Spinning up

Regardless the way you going to run this project, you must create a `.env` file like below:

```dotenv
SECRET_KEY=yourSuperSecret
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
DEBUG=1
DJANGO_ALLOWED_HOSTS='localhost 127.0.0.1 [::1]'
```
For simplicity `SECRET_KEY` is used as a Bearer token to authenticate on the API.

### Docker

For `development` mode, just run
```shell
docker-compose up -d --build
```

At the end you will be able to check the API documentation here: http://localhost:8000/api/docs

For `production` purposes, create an `.env.prod` file with other data,
such as DEBUG=0, a new SECRET_KEY and possible other db info.
For this mode, you'll have to run `docker-compose` like below:

```shell
docker-compose -f docker-compose.prod.yml up -d --build
```

Also, bear in mind that, differently from the dev mode, migrations are not executed everytime, 
so you'll have to run it manually. For a docker container, run:

```shell
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```

### Manually

Install `poetry` into your machine and run

```
poetry install
```

Remember that you'll have to has an Postgres instance on your machine.
