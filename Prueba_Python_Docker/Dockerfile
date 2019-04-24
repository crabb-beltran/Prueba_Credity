#https://hub.docker.com/
#docker pull ubuntu
#docker build -t <nombre_imagen> .

FROM ubuntu:latest

MAINTAINER Cristian Beltran

RUN apt-get update

RUN  apt-get install -y python3.6

RUN apt-get install -y python3-pip

WORKDIR /

COPY ./python /

CMD python3 /Fibonacci.py
CMD python3 /Pascal.py
