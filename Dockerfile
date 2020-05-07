FROM python:3.7
ARG DB_USER
ARG DB_PASSWORD

RUN mkdir -p /opt/source
COPY . /opt/source
WORKDIR /opt/source

RUN pip3 install -r requirements.txt 


ENTRYPOINT python3 manage.py runserver 0.0.0.0:8000