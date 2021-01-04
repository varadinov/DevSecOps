FROM centos:7
EXPOSE 80
RUN yum update -y
WORKDIR /code
ADD . /code
RUN touch index.html
CMD python index.py