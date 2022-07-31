
FROM python:latest

RUN mkdir /app
WORKDIR /app/

COPY req.txt .

RUN pip install -r req.txt

COPY . /app