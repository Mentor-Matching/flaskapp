FROM jazzdd/alpine-flask:python3

WORKDIR /mm-backend

ADD scripts/init.sh ./init.sh
RUN chmod +x ./init.sh

ADD requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

ADD app.py ./app.py
ADD flaskapp ./flaskapp

EXPOSE 80

ENTRYPOINT [ "./init.sh" ]
