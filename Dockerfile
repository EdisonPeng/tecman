FROM ubuntu:latest

RUN apt-get update
RUN apt install software-properties-common --assume-yes
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt install python3.7 --assume-yes
RUN apt install python3-pip --assume-yes
RUN apt-get install vim --assume-yes
RUN python3.7 -m pip install django
