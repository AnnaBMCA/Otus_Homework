FROM python:3.9-buster

WORKDIR /homework_03

COPY requirements.txt requirements.txt
COPY . .

RUN pip install -r requirements.txt

CMD uvicorn app:app --host=0.0.0.0