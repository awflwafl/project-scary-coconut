FROM python:3.7.4-alpine3.9

WORKDIR /usr/src/app

COPY . .

EXPOSE 80

RUN pip install --no-cache-dir pipenv
RUN pipenv install --deploy --dev --ignore-pipfile --system
