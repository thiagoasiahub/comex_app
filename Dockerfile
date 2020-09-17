FROM python:3.7.2
ENV PYTHONUNBUFFERED 1
RUN mkdir /comex
WORKDIR /comex
ADD requirements.txt /comex/

RUN pip install -U pip
RUN pip install -r requirements.txt

ADD . /app/