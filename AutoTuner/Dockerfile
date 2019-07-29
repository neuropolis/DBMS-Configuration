FROM ubuntu:16.04
MAINTAINER wondervictor "victorchanchinag@gmail.com"

RUN apt-get -y update
RUN apt-get -y install python-pip
RUN apt-get -y install software-properties-common
RUN add-apt-repository 'deb http://archive.ubuntu.com/ubuntu trusty universe'
RUN apt-get -y update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server-5.6

RUN pip install --upgrade pip
RUN apt-get -y install libmysqlclient-dev
COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install -r requirements.txt

WORKDIR /home/AutoTuner
