FROM python:3.9.5-slim-buster

RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install -y systemd bash curl

WORKDIR /backend

ADD scripts/init.sh ./init.sh
RUN chmod +x ./init.sh

ADD requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

ADD app.py ./app.py
ADD flaskapp ./flaskapp

EXPOSE 80

ENTRYPOINT [ "./init.sh" ]
