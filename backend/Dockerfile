FROM python:3.7-slim

RUN python -m pip install --upgrade pip

RUN  apt-get -y update && apt-get install -y libzbar-dev

RUN mkdir /backend
 WORKDIR /backend
 ADD requirements.txt /backend/
 RUN python -m pip install -r requirements.txt
 ADD . /backend/
 EXPOSE 8000
