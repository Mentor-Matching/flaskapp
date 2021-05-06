FROM python:3.9.5-slim-buster

# FROM jazzdd/alpine-flask:python3
# FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine3.7
# RUN apk add --upgrade --no-cache alpine-sdk libffi libffi-dev
# RUN apk add gcc musl-dev python3-dev openssl-dev cargo
# RUN pip install --upgrade pip setuptools wheel
RUN pip install --upgrade pip
# RUN apk add mysql mysql-client
RUN apt-get update
RUN apt-get install -y mariadb-server
RUN apt-get install -y systemd bash curl nano

WORKDIR /backend

ADD scripts/setup_mariadb.sh ./setup_mariadb.sh
RUN chmod +x ./setup_mariadb.sh
ADD scripts/init.sh ./init.sh
RUN chmod +x ./init.sh

ADD requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

ADD app.py ./app.py
ADD flaskapp ./flaskapp

EXPOSE 5000

ENTRYPOINT [ "./init.sh" ]
