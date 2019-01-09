FROM python:3

MAINTAINER Christopher Bianchi

WORKDIR /usr/src/app

ENV PYTHONPATH /usr/src/app

COPY ./source ./

RUN pip install -r requirements.txt

CMD ["python", "wsgi.py"]
