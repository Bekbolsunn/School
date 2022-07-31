
FROM python:latest

RUN mkdir /app
WORKDIR /app/

COPY req.txt .

RUN pip install -r requirements.txt

COPY . /app