FROM python:3.6

RUN mkdir /code

WORKDIR /code
COPY requirements.txt /code
RUN pip install -U pip \
    && pip install -r /code/requirements.txt

COPY . /code
