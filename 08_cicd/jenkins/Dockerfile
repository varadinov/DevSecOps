FROM centos:centos8 as base
RUN yum update -y && yum install python3 python3-pip python3-devel gcc -y 

FROM base as python

EXPOSE 8080

ADD . /app
WORKDIR /app
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

CMD [ "uwsgi", "--http", "0.0.0.0:8080", \
    "--workers", "1", \
    "--threads", "5", \
    "--plugins", "python3", \
    "--protocol", "uwsgi", \
    "--disable-logging", \
    "--wsgi", "app:app" ] 
